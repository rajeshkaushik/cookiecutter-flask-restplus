from flask import Blueprint, jsonify, url_for

from {{cookiecutter.app_name}} import __version__


healthcheck = Blueprint("healthcheck", __name__)


@healthcheck.route("")
def index():
    return jsonify({
        'version': __version__,
        'docs': [
            {
                'url': url_for('api_1_0.specs')
            }
        ]})
