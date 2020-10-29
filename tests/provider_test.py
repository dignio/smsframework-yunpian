# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from flask import Flask
from freezegun import freeze_time
import responses

from smsframework import Gateway, OutgoingMessage
from smsframework.providers import NullProvider
from smsframework_yunpian import YunpianProvider


class YunpianProviderTest(unittest.TestCase):
    def setUp(self):
        # Gateway
        gw = self.gw = Gateway()
        gw.add_provider('null', NullProvider)  # provocation
        gw.add_provider('main', YunpianProvider, apikey='my_api_key1234')

        # Flask
        app = self.app = Flask(__name__)

        # Register receivers
        gw.receiver_blueprints_register(app, prefix='/a/b/')

    @responses.activate
    def test_send(self):
        """ Test message send """
        gw = self.gw
        ok_json = {
            'code': 0,
            'msg': 'OK',
            'count': 1,
            'fee': 0.05,
            'unit': 'RMB',
            'mobile': '123456',
            'sid': 16741236146
        }
        responses.add(
                responses.POST,
                'https://sms.yunpian.com/v2/sms/single_send.json',
                json=ok_json,
                status=200,)

        message = gw.send(OutgoingMessage('+123456', 'hey', src='dignio', provider='main'))
        self.assertEqual(len(responses.calls), 1)
        self.assertIn('my_api_key1234', responses.calls[0].request.body)
        self.assertEqual(message.msgid, 16741236146)

    @responses.activate
    def test_error_send(self):
        """ Test message send """
        gw = self.gw
        bad_json = {
            'code': 2,
            'msg': 'Required parameter has format error',
            'detail': 'Format the parameter by prompt.'
        }
        responses.add(
                responses.POST,
                'https://sms.yunpian.com/v2/sms/single_send.json',
                json=bad_json,
                status=200,)

        try:
            message = gw.send(OutgoingMessage('+123456', 'hey', src='dignio', provider='main'))
            assert False
        except Exception as e:
            self.assertIn('2 Required parameter has format error', str(e))

        self.assertEqual(len(responses.calls), 1)
        self.assertIn('my_api_key1234', responses.calls[0].request.body)
