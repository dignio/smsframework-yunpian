# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from flask import Flask
from freezegun import freeze_time

from smsframework import Gateway, OutgoingMessage
from smsframework.providers import NullProvider
from smsframework_yunpian import YunpianProvider


class YunpianProviderTest(unittest.TestCase):
    def setUp(self):
        # Gateway
        gw = self.gw = Gateway()
        gw.add_provider('null', NullProvider)  # provocation
        gw.add_provider('main', YunpianProvider, user='kolypto', password='1234')

        # Flask
        app = self.app = Flask(__name__)

        # Register receivers
        gw.receiver_blueprints_register(app, prefix='/a/b/')

    def test_send(self):
        """ Test message send """
        gw = self.gw
        self.assertTrue(False, 'Implement the test!')
