import logging

from flask import Flask
from flask_restplus.apidoc import apidoc
from flask.logging import default_handler


ROOT_URL = '/{{cookiecutter.app_name}}'


def create_app(config_name):

    from {{cookiecutter.app_name}}.config import app_config

    config = app_config[config_name]

    app = Flask(__name__)
    app.config.from_object(config)
    app.config["APPLICATION_ROOT"] = ROOT_URL

    # Flask restplus uses apidoc to generate URLs for static files in swagger.
    #
    # If any of the follwing is true:
    #   1. apidoc is not registered as a blueprint (default use case)
    #   2. apidoc is registered after another blueprint,
    # restplus auto-registers the default apidoc at '/'.
    #
    # Hence, the `apidoc` should be the first blueprint registered. And it is
    # mounted at ROOT_URL
    app.register_blueprint(apidoc, url_prefix=ROOT_URL)

    with app.app_context():
        from {{cookiecutter.app_name}}.api_v1 import blueprint as api
        from {{cookiecutter.app_name}}.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL + '/v1')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')

    # set custom log format
    from {{cookiecutter.app_name}}.custom_logging import get_custom_formatter
    formatter = get_custom_formatter(config)
    default_handler.setFormatter(formatter)

    # Enable error logs push to configured slack channel
    if app.config.get('SLACK_TOKEN') and app.config.get('SLACK_CHANNEL'):
        from {{cookiecutter.app_name}}.custom_logging import get_slack_error_handler
        handler = get_slack_error_handler(config)
        app.logger.addHandler(handler)

    app.logger.setLevel(app.config['APP_LOG_LEVEL'])

    return app
