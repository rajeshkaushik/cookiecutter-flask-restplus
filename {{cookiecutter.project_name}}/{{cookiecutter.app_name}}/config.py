import os
import logging
from typing import Optional

HOST = os.getenv('APP_HOST', '0.0.0.0')
PORT = os.getenv('APP_PORT', '8350')

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', b'\xfapO\xed\xac\xab\x1fAO\x06\xb5\xfc[\xcb\xb4\x0b)\xd6I\x9b\xb0A\xf1\x07')

    APIKEY_REQUIRED = False
    APIKEY = os.environ['APIKEY'] if APIKEY_REQUIRED else None

    API_DOCS_URL = '/doc/'  # type: Optional[str]

    LOG_FORMAT = (
        '[%(asctime)s] %(levelname)s in %(filename)s:%(lineno)d '
        '%(message)s')

    EXCLUDE_HEADERS_FROM_LOG = ['Apikey']

    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')

    APP_LOG_LEVEL = logging.INFO

    URL_TO_IGNORE = [API_DOCS_URL, 'swagger.json']
    ENABLE_REQUEST_DATA_LOG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    SLACK_TOKEN = 'SLACK_TOKEN'
    SLACK_CHANNEL = 'SLACK_CHANNEL'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    APIKEY = '0470e318-5c1e-427e-8119-edff81e23c03'


class QaConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    API_DOCS_URL = None


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'qa': QaConfig,
    'stag': StagingConfig,
    'production': ProductionConfig,
}
