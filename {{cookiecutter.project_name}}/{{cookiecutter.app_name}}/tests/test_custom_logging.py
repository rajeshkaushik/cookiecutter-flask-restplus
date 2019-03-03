import logging
import os

from flask import current_app
from flask.logging import default_handler
from unittest.mock import patch

from {{cookiecutter.app_name}}.tests.conftest import AppTestCase
from {{cookiecutter.app_name}}.custom_logging import SlackLogHandler


class CustomLogTestCase(AppTestCase):

    def test_custom_log_format(self):
        self.assertEqual(current_app.config['LOG_FORMAT'], default_handler.formatter._fmt)

    def test_custom_log_level(self):
        self.assertEqual(current_app.config['APP_LOG_LEVEL'], current_app.logger.level)

    def test_slack_log_handler(self):
        self.assertEqual(current_app.logger.handlers[0].__class__, SlackLogHandler)
