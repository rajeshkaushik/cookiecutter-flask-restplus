import os

from werkzeug.contrib.fixers import ProxyFix

from {{cookiecutter.app_name}}.app import create_app
{%- if cookiecutter.newrelic == 'y' %}
import newrelic.agent
{%- endif %}


config_name = os.getenv('FLASK_ENV')

{%- if cookiecutter.newrelic == 'y' %}
newrelic_conf_file = os.getenv('NEWRELIC_INI_PATH')
if newrelic_conf_file:
    newrelic.agent.initialize(
        newrelic_conf_file,
        environment=config_name,
        log_file='stderr'
    )
{%- endif %}

app = create_app(config_name)

app.wsgi_app = ProxyFix(app.wsgi_app)
