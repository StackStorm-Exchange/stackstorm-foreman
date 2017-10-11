#!/usr/bin/env python
import argparse
import collections
import datetime
import glob
import inspect
import jinja2
import json
import os
import re
import urllib3
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

urllib3.disable_warnings()

from foreman.client import Foreman
from foreman.client import Resource

FOREMAN_SERVER   = os.environ.get('FOREMAN_SERVER')
FOREMAN_USERNAME = os.environ.get('FOREMAN_USERNAME')
FOREMAN_PASSWORD = os.environ.get('FOREMAN_PASSWORD')

API_DEFINITION_GLOB_PATH = "./api_definitions*"
ACTION_TEMPLATE_PATH = "./action.j2.yaml"
ACTION_DIRECTORY = "../actions"


class Cli:
    def parse(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        # Subparsers
        subparsers = parser.add_subparsers(dest="command")

        # fetch-api
        fetch_parser = subparsers.add_parser('fetch-api',
                                             help="Retrieves the API definitions from a running server")
        fetch_parser.add_argument('-s', '--server', default=FOREMAN_SERVER,
                                  help="Hostname/ip of the Foreman server",
                                  required=True)
        fetch_parser.add_argument('-u', '--username', default=FOREMAN_USERNAME,
                                  help="Username to login to the Foreman server",
                                  required=True)
        fetch_parser.add_argument('-p', '--password', default=FOREMAN_PASSWORD,
                                  help="Password to login to the Foreman server")


        # generate
        generate_parser = subparsers.add_parser('generate',
                                             help="Generates actions for the Foreman API")
        action_dir = os.path.join(os.path.dirname(__file__), '..', 'actions')
        generate_parser.add_argument('-s', '--server', default=FOREMAN_SERVER,
                                     help="Hostname/ip of the Foreman server",
                                     required=True)
        generate_parser.add_argument('-u', '--username', default=FOREMAN_USERNAME,
                                     help="Username to login to the Foreman server",
                                     required=True)
        generate_parser.add_argument('-p', '--password', default=FOREMAN_PASSWORD,
                                     help="Password to login to the Foreman server")
        generate_parser.add_argument('-d', '--directory', default=action_dir,
                                     help="Directory where actions should be written to")
        generate_parser.add_argument('-a', '--api-definition',
                                     help=("Path to the API defitions directory retrieved from 'fetch-api'."
                                           " If unspecified, we'll lookup the newest one based on file name."))

        # examples
        subparsers.add_parser('examples',
                              help="Prints examples of how to use this script to stdout")

        args = parser.parse_args()
        if args.command == "examples":
            self.examples()
            exit(0)
        return args

    def examples(self):
        print "examples:\n"\
            "  # gerenate actions from the server/\n"\
            "  ./generate_actions.py generate\n"\
            "\n"\
            "  # gerenate actions into an alternate directory from a specific WSDL/\n"\
            "  ./generate_actions.py generate -d ../actions_new -w menandmice_wsdl_new.xml\n"\



class MyYAML(YAML):
    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()

class ActionGenerator(object):

    def __init__(self, cli_args, **kwargs):
        self.cli_args = cli_args

    def fetch_api(self):
        now = datetime.datetime.now()
        api_definition = "./api_definitions_{}".format(now.strftime('%Y_%m_%d'))
        print "Using cache dir {}".format(api_definition)
        self.client = Foreman('https://{}/'.format(self.cli_args.server),
                              auth=(self.cli_args.username, self.cli_args.password),
                              api_version=2,
                              use_cache=False,
                              cache_dir=api_definition)

    def generate(self):
        api_definition = self.cli_args.api_definition
        if not api_definition:
            api_definition_list = glob.glob(API_DEFINITION_GLOB_PATH)
            # find newest wsdl (by name)
            api_definition = max(api_definition_list)

        self.client = Foreman('https://{}/'.format(self.cli_args.server),
                              auth=(self.cli_args.username, self.cli_args.password),
                              api_version=2,
                              use_cache=True,
                              cache_dir=api_definition)

        # all methods of the client
        unused = {'methods': [],
                  'unknown_extras': []}
        results = {'resources': [],
                   'special_attributes': []}
        special_attributes = ['api_version', 'version']
        for attr in inspect.getmembers(self.client):
            if inspect.ismethod(attr[1]):
                unused['methods'].append(attr)
            elif isinstance(attr[1], Resource):
                if attr[0] == "":
                    continue
                results['resources'].append(attr)
            elif attr[0] in special_attributes:
                results['special_attributes'].append(attr)
            else:
                unused['unknown_extras'].append(attr)

        # resources
        self.generate_resources(results['resources'])


    def generate_resources(self, resource_list):
        methods = []
        for resource_name, resource in resource_list:
            for member_name, member in inspect.getmembers(resource):
                if ((member_name in resource._own_methods) or
                    (not member_name.startswith('_'))):
                    method_def = member.defs
                    method = {'name': '{}_{}'.format(method_def.resource,
                                                     method_def.name),
                              'operation': '{}.{}'.format(method_def.resource,
                                                          method_def.name),
                              'description': '{} (resource: {} {})'.format(method_def.short_desc,
                                                                           method_def.http_method,
                                                                           method_def.url)}

                    method['parameters'] = self.parse_params(method_def.params)
                    self.render_action(method)
                    methods.append(method)

    def parse_param_type(self, param_type):
        t = param_type
        if t == 'hash':
            t = 'object'
        return t

    def dict_to_yaml(self, d):
        yaml = MyYAML()
        yaml.indent(sequence=4, offset=2)
        return yaml.dump(d)

    def clean_desc(self, desc):
        from HTMLParser import HTMLParser
        htmlparser = HTMLParser()
        desc = desc.encode('punycode')
        desc = htmlparser.unescape(desc)
        desc = desc.replace('\n', '')
        regex = re.compile('<.*?>')
        desc = re.sub(regex, '', desc)
        if not desc:
            return None
        return desc

    def parse_params(self, params):
        parameters = self.gather_params(params)
        for param in parameters:
            if 'parameters' in param:
                sub_params_str = self.dict_to_yaml(param['parameters'])
                sub_params_str = sub_params_str.replace('\n', '\n            ')
                param['description'] = (">\n"
                                        "       'description: {0}\n"
                                        "        parameters:\n"
                                        "            {1}'".format(param['description'],
                                                                  sub_params_str))

        return parameters


    def gather_params(self, params):
        parameters = []
        for param in params:
            p = dict()
            p['name'] = param['name']
            p['description'] = self.clean_desc(param['description'])
            p['required'] = param['required']
            p['type']= self.parse_param_type(param['expected_type'])

            if 'params' in param:
                p['parameters'] = self.gather_sub_params(param['params'])

            parameters.append(p)
        return parameters

    def gather_sub_params(self, sub_params):
        parameters = {}
        for param in sub_params:
            p = dict()
            p['description'] = self.clean_desc(param['description'])
            p['required'] = param['required']
            p['type']= self.parse_param_type(param['expected_type'])

            if 'params' in param:
                p['parameters'] = self.gather_sub_params(param['params'])

            parameters[param['name']] = p
        return parameters

    def jinja_render_file(self, filename, context):
        path, filename = os.path.split(filename)
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(path or './')
        ).get_template(filename).render(context)

    def jinja_render_str(self, jinja_template_str, context):
        return jinja2.Environment().from_string(jinja_template_str).render(context)

    def render_action(self, context):
        # print self.jinja_render_file(ACTION_TEMPLATE_PATH, context)
        action_data = self.jinja_render_file(ACTION_TEMPLATE_PATH, context)
        action_filename = "{}/{}.yaml".format(ACTION_DIRECTORY,
                                              context['name'])
        with open(action_filename, "w") as f:
            f.write(action_data)


    def run(self):
        if self.cli_args.command == "fetch-api":
            self.fetch_api()
        elif self.cli_args.command == "generate":
            self.generate()
        else:
            raise RuntimeError("Unknown command {}".format(self.cli_args.command))


if __name__ == "__main__":
    cli = Cli()
    args = cli.parse()
    generator = ActionGenerator(args)
    generator.run()
