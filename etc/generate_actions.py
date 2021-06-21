#!/usr/bin/env python
import argparse
import datetime
import glob
import inspect
import jinja2
import os
import re
from six.moves.html_parser import HTMLParser

import urllib3

from foreman.client import Foreman
from foreman.client import Resource
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

urllib3.disable_warnings()


FOREMAN_SERVER = os.environ.get('FOREMAN_SERVER')
FOREMAN_USERNAME = os.environ.get('FOREMAN_USERNAME')
FOREMAN_PASSWORD = os.environ.get('FOREMAN_PASSWORD')

API_DEFINITION_GLOB_PATH = "./api_definitions*"
ACTION_TEMPLATE_PATH = "./action.yaml.j2"
ACTION_DIRECTORY = "../actions"

TABLE_TEMPLATE_PATH = "./action_table.md.j2"
TABLE_FILE_PATH = "./action_table.md"


class Cli:
    def parse(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        # Subparsers
        subparsers = parser.add_subparsers(dest="command")

        # fetch-api
        fetch_parser = subparsers.add_parser('fetch-api',
                                             help=("Retrieves the API definitions"
                                                   " from a running server"))
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
                                     help="Hostname/ip of the Foreman server")
        generate_parser.add_argument('-u', '--username', default=FOREMAN_USERNAME,
                                     help="Username to login to the Foreman server")
        generate_parser.add_argument('-p', '--password', default=FOREMAN_PASSWORD,
                                     help="Password to login to the Foreman server")
        generate_parser.add_argument('-d', '--directory', default=action_dir,
                                     help="Directory where actions should be written to")
        generate_parser.add_argument('-a', '--api-definition',
                                     help=("Path to the API defitions directory"
                                           " retrieved from 'fetch-api'. If unspecified,"
                                           " we'll lookup the newest one based on file name."))

        # examples
        subparsers.add_parser('examples',
                              help="Prints examples of how to use this script to stdout")

        args = parser.parse_args()
        if args.command == "examples":
            self.examples()
            exit(0)
        return args

    def examples(self):
        print("examples:\n"
              "  # fetch api definitions from the server/\n"
              "  ./generate_actions.py fetch-api -s foreman.domain.tld -u admin -p xxx\n"
              "\n"
              "  # gerenate actions from the fetched (cached) api/\n"
              "  ./generate_actions.py generate -a ./api_definitions_2017_09_15/\n"
              "\n"
              "  # gerenate actions directly from the server/\n"
              "  ./generate_actions.py generate -s foreman.domain.tld -u admin -p xxx\n")


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
        self.action_template_params = self.load_template_params()
        self.api_version = 2

    def load_template_params(self):
        params_yaml_str = self.jinja_render_file(ACTION_TEMPLATE_PATH,
                                                 {'name': ''})
        yaml = MyYAML()
        params_dict = yaml.load(params_yaml_str)  # pylint: disable=no-member
        params = params_dict['parameters'].keys()
        return params

    def fetch_api(self):
        now = datetime.datetime.now()
        api_definition = "./api_definitions_{}".format(now.strftime('%Y_%m_%d'))
        print("Using cache dir {}".format(api_definition))
        self.client = Foreman('https://{}/'.format(self.cli_args.server),
                              auth=(self.cli_args.username, self.cli_args.password),
                              api_version=self.api_version,
                              use_cache=False,
                              cache_dir=api_definition)

    def generate(self):
        api_definition = self.cli_args.api_definition
        if not api_definition:
            api_definition_list = glob.glob(API_DEFINITION_GLOB_PATH)
            # find newest api def (by name)
            api_definition = max(api_definition_list)
            self.client = Foreman('https://{}/'.format(self.cli_args.server),
                                  auth=(self.cli_args.username, self.cli_args.password),
                                  api_version=2,
                                  use_cache=True,
                                  cache_dir=api_definition)
        else:
            defs_path = os.path.join(api_definition, 'definitions')
            api_def_paths = glob.glob('{}/*-v{}.json'.format(defs_path, self.api_version))
            for p in api_def_paths:
                # Filename fetched from fetch_api() has the following pattern:
                # <version>-<api_version>.json
                #
                # Example:
                #  Satellite-v2.json
                #  1.15.1-v2.json
                #
                # We need to pass in <version> and <api_version> into the Foreman()
                # constructure, so the following code pulls those variables from
                # the filename.
                api_def = os.path.basename(p)
                api_def = api_def.replace('.json', '')
                api_def_parts = api_def.split('-')
                self.version = api_def_parts[0]
                self.api_version = api_def_parts[1].replace('v', '')
                break

            self.client = Foreman('https://usingcache/',
                                  version=self.version,
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

        # get all of the methods
        method_defs = self.gather_method_defs(results['resources'])

        # convert the methods into actions
        self.render_method_defs_into_actions(method_defs)
        self.render_method_defs_into_table(method_defs)

    def gather_method_defs(self, resource_list):
        method_defs = []
        for resource_name, resource in resource_list:
            for member_name, member in inspect.getmembers(resource):
                if (((member_name in resource._own_methods) or
                     (not member_name.startswith('_')))):
                    method_defs.append(member.defs)
        return method_defs

    def generate_action_name(self, method_def):
        return "{}.{}".format(method_def.resource, method_def.name)

    def render_method_defs_into_actions(self, method_defs):
        for method_def in method_defs:
            action_name = self.generate_action_name(method_def)
            action = {'name': action_name,
                      'operation': '{}.{}'.format(method_def.resource,
                                                  method_def.name),
                      'description': '{} (resource: {} {})'.format(method_def.short_desc,
                                                                   method_def.http_method,
                                                                   method_def.url),
                      'entry_point': 'lib/action.py'}
            action['parameters'] = self.parse_params(method_def.params)
            print(action['operation'])

            for param in action['parameters']:
                if param['name'] in self.action_template_params:
                    raise RuntimeError("Parameter '{}' conflicts with the builtin"
                                       " parameter in action '{}'.".format(param['name'],
                                                                           action_name))

            self.render_action(action)

    def delete_table_file(self):
        try:
            os.remove(TABLE_FILE_PATH)
        except OSError:
            pass

    def create_table_file(self):
        with open(TABLE_FILE_PATH, "a+") as f:
            f.write(("| Action | Foreman API | Description |\n"
                     "|--------|-------------|-------------|\n"))

    def render_method_defs_into_table(self, method_defs):
        self.delete_table_file()
        self.create_table_file()

        foreman_url = 'https://theforeman.org/api/1.16/'
        katello_url = 'https://theforeman.org/plugins/katello/3.4/api/'

        for method_def in method_defs:
            action_name = self.generate_action_name(method_def)
            method_doc_url = method_def._method['doc_url']
            method_doc_url = method_doc_url.replace('../', '')
            base_url = None
            if method_def.url.startswith('/katello/'):
                base_url = katello_url
            else:
                base_url = foreman_url
            method_doc_url = base_url + method_doc_url + '.html'
            context = {'name': action_name,
                       'url': method_def.url,
                       'http_method': method_def.http_method,
                       'description': method_def.short_desc,
                       'reference_url': method_doc_url}
            self.render_table_entry(context)

    def parse_param_type(self, param_type):
        t = param_type
        if t == 'hash':
            t = 'object'
        elif t == 'numeric':
            t = 'number'
        return t

    def dict_to_yaml(self, d):
        yaml = MyYAML()
        # have it indent arrays with an extra couple of spaces
        yaml.indent(sequence=4, offset=2)  # pylint: disable=no-member
        # prevent line wrapping
        yaml.width = 99999
        return yaml.dump(d)

    def clean_desc(self, desc):
        if not desc:
            return ''

        # there were a few description strings with unicode characters (quotes)
        # this removes them
        desc = desc.replace(u"\u201c", '"').replace(u"\u201d", '"')
        desc = desc.replace('\n', '')
        desc = desc.replace('"', "'")

        # convert HTML escaped sequences into ascii
        htmlparser = HTMLParser()
        desc = htmlparser.unescape(desc)

        # remove HTML tags
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
                desc = self.clean_desc(param['description'])
                param['description'] = (">\n"
                                        "       \"description: {0}\n"
                                        "        parameters:\n"
                                        "            {1}\"".format(desc,
                                                                   sub_params_str))
            elif param['description']:
                param['description'] = '"' + self.clean_desc(param['description']) + '"'

        return parameters

    def gather_params(self, params):
        parameters = []
        for param in params:
            p = dict()
            p['name'] = param['name']
            p['description'] = self.clean_desc(param['description'])
            p['required'] = param['required']
            p['type'] = self.parse_param_type(param['expected_type'])

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
            p['type'] = self.parse_param_type(param['expected_type'])

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
        action_data = self.jinja_render_file(ACTION_TEMPLATE_PATH, context)
        action_filename = "{}/{}.yaml".format(ACTION_DIRECTORY,
                                              context['name'])
        with open(action_filename, "w") as f:
            f.write(action_data)

    def render_table_entry(self, context):
        table_data = self.jinja_render_file(TABLE_TEMPLATE_PATH, context)
        with open(TABLE_FILE_PATH, "a+") as f:
            f.write(table_data + "\n")

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
