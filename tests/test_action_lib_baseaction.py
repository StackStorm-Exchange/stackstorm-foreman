from foreman_base_action_test_case import ForemanBaseActionTestCase
from lib.action import BaseAction, CONFIG_CONNECTION_KEYS

import copy
import mock


class TestActionLibBaseAction(ForemanBaseActionTestCase):
    __test__ = True
    action_cls = BaseAction

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, BaseAction)

    def test__get_del_arg_present(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key1"
        expected_dict = {"key2": "value2"}
        expected_value = test_dict["key1"]
        result_value = action._get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test__get_del_arg_missing(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key3"
        expected_dict = test_dict
        expected_value = None
        result_value = action._get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test__resolve_connection_from_config(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['foreman'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        kwargs_dict = {'connection': connection_name}
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_config_missing(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'this_connection_doesnt_exist'
        kwargs_dict = {'connection': connection_name}
        with self.assertRaises(KeyError):
            action._resolve_connection(kwargs_dict)

    def test__resolve_connection_from_config_defaults(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['foreman'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        kwargs_dict = {'connection': connection_name}
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_kwargs(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'username': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test__resolve_connection_from_kwargs_defaults(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'username': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test__resolve_connection_from_kwargs_extras(self):
        action = self.get_action_instance(self.config_blank)
        connection_expected = {'connection': None,
                               'server': 'kwargs_server',
                               'username': 'kwargs_user',
                               'password': 'kwargs_password'}
        kwargs_dict = copy.deepcopy(connection_expected)
        kwargs_extras = {"extra_key1": "extra_value1",
                         "extra_key2": 234}
        kwargs_dict.update(kwargs_extras)
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, kwargs_extras)

    def test__validate_connection(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if required:
                connection[key] = "value_for_key_{}".format(key)

        result = action._validate_connection(connection)
        self.assertTrue(result)

    def test__validate_connection_missing_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        with self.assertRaises(KeyError):
            action._validate_connection(connection)

    def test__validate_connection_none_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key, required, default in CONFIG_CONNECTION_KEYS:
            connection[key] = None

        with self.assertRaises(KeyError):
            action._validate_connection(connection)

    @mock.patch('lib.action.foreman.client.Foreman')
    def test_run(self, mock_foreman):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection = self.config_good['foreman'][connection_name]
        operation = 'member.func'

        op_args = {'op_arg1': 'abc',
                   'op_arg2': [1, 2, 3]}
        kwargs_dict = {'operation': operation,
                       'connection': connection_name}
        kwargs_dict.update(op_args)

        op_result = 'abc'

        mock_func = mock.MagicMock()
        mock_func.return_value = op_result
        mock_member = mock.MagicMock(func=mock_func)
        mock_client = mock.MagicMock(member=mock_member)
        mock_foreman.return_value = mock_client

        result = action.run(**kwargs_dict)

        self.assertEqual(result, op_result)
        mock_foreman.assert_called_with('https://{}/'.format(connection['server']),
                                        auth=(connection['username'], connection['password']),
                                        api_version=2)
        mock_func.assert_called_with(**op_args)
