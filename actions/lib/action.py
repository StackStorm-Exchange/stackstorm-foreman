#!/usr/bin/env python

from foreman.client import Foreman
from st2actions.runners.pythonrunner import Action
import operator
import requests
import urllib3

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()   # pylint: disable=no-member

#                         (key, required, default)
CONFIG_CONNECTION_KEYS = [('server', True, ""),
                          ('username', True, ""),
                          ('password', True, "")]


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config=config)

    def _get_del_arg(self, key, kwargs_dict):
        """Attempts to retrieve an argument from kwargs with key.
        If the key is found, then delete it from the dict.
        :param key: the key of the argument to retrieve from kwargs
        :returns: The value of key in kwargs, if it exists, otherwise None
        """
        if key in kwargs_dict:
            value = kwargs_dict[key]
            del kwargs_dict[key]
            return value
        else:
            return None

    def _resolve_connection(self, kwargs_dict):
        """Attempts to resolve the connection information by looking up information
        from action input parameters (highest priority) or from the config (fallback).
        :param kwargs_dict: dictionary of kwargs containing the action's input
        parameters
        :returns: a dictionary with the connection parameters (see: CONFIG_CONNECTION_KEYS)
        resolved.
        """
        connection_name = self._get_del_arg('connection', kwargs_dict)
        config_connection = None
        if connection_name:
            config_connection = self.config['foreman'].get(connection_name)
            if not config_connection:
                raise KeyError("config.yaml missing connection: foreman:{0}"
                               .format(connection_name))

        action_connection = {'connection': connection_name}

        # Override the keys in creds read in from the config given the
        # override parameters from the action itself
        # Example:
        #   'user' parameter on the action will override the username
        #   from the credential. This is useful for runnning the action
        #   standalone and/or from the commandline
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if key in kwargs_dict and kwargs_dict[key]:
                # use params from cmdline first (override)
                action_connection[key] = self._get_del_arg(key, kwargs_dict)
            elif config_connection and key in config_connection and config_connection[key]:
                # fallback to creds in config
                action_connection[key] = config_connection[key]
            else:
                if not required and default:
                    action_connection[key] = default

            # remove the key from kwargs if it's still in there
            if key in kwargs_dict:
                del kwargs_dict[key]

        return action_connection

    def _validate_connection(self, connection):
        """Ensures that all required parameters are in the connection. If a
        required parameter is missing a KeyError exception is raised.
        :param connection: connection to validate
        :returns: True if the connection is valid
        """
        for key, required, default in CONFIG_CONNECTION_KEYS:
            # ensure the key is present in the connection?
            if key in connection and connection[key]:
                continue

            # skip if this key is not required
            if not required:
                continue

            if 'connection' in connection:
                raise KeyError("config.yaml mising: foreman:{0}:{1}"
                               .format(connection['connection'], key))
            else:
                raise KeyError("Because the 'connection' action parameter was"
                               " not specified, the following action parameter"
                               " is required: {0}".format(key))
        return True

    def run(self, **kwargs):
        kwargs_dict = dict(kwargs)

        # parse parameters
        operation = self._get_del_arg('operation', kwargs_dict)
        connection = self._resolve_connection(kwargs_dict)
        self._validate_connection(connection)

        # connect to the server
        client = Foreman('https://{}/'.format(connection['server']),
                         auth=(connection['username'], connection['password']),
                         api_version=2)

        # Performs a "deep" getattr() lookup so we can pass a string like
        # 'method1.method2.method3' without having to chain getattr()
        # calls.
        op = operator.attrgetter(operation)(client)
        return op(**kwargs_dict)
