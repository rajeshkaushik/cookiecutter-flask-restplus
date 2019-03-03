from werkzeug.exceptions import NotFound, MethodNotAllowed
from flask import Blueprint, current_app, request
from flask_restplus import Api

from {{cookiecutter.app_name}}.api import ns
from {{cookiecutter.app_name}}.custom_error_message import custom_abort, get_error_messages
from {{cookiecutter.app_name}}.custom_logging import format_headers


blueprint = Blueprint('api_1_0', __name__)


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'APIKEY'
    }
}


api = Api(
    blueprint,
    doc=current_app.config['API_DOCS_URL'],
    catch_all_404s=True,
    authorizations=authorizations, security='apikey'
)
api.namespaces.clear()
api.add_namespace(ns)


@blueprint.before_request
def validate_apikey():
    # Log the request headers and data
    if current_app.config['ENABLE_REQUEST_DATA_LOG']:
        current_app.logger.info(
            '%s %s Headers: %s Data: %s', request.method, request.full_path,
            format_headers(request.headers, current_app.config['EXCLUDE_HEADERS_FROM_LOG']), request.json)

    # Remove check for APIKEY header for docs
    url_to_ignore = current_app.config['URL_TO_IGNORE']
    if any(key in request.path for key in url_to_ignore):
        return

    if current_app.config['APIKEY_REQUIRED']:
        configured_api_key = current_app.config['APIKEY']
        apikey = request.headers.get(authorizations['apikey']['name'])
        if configured_api_key != apikey:
            custom_abort(
                401,
                'Unauthorized',
                'You are not authorized to access this API',
                'Authorization Error'
            )
    return


@blueprint.after_request
def after_request(response):
    code = response.status_code
    if code < 200 or code >= 300:
        current_app.logger.error(
            '%s %s %s Headers: %s Data: %s Response: %s', code, request.method,
            request.full_path,
            format_headers(request.headers, current_app.config['EXCLUDE_HEADERS_FROM_LOG']),
            request.json, response.json
        )
    return response


def log_error_message(error):

    log = {
        'PATH': request.path,
        'METHOD': request.method,
        'EXCEPTION': repr(error),
        'DATA': request.json
    }
    current_app.logger.error(log)


@api.errorhandler(NotFound)
def error_404_handler(error):
    log_error_message(error)
    messages = get_error_messages(repr(error), repr(error))

    return {'messages': messages}, getattr(error, 'code', 404)


@api.errorhandler(MethodNotAllowed)
def error_405_handler(error):
    log_error_message(error)
    messages = get_error_messages(repr(error), repr(error))

    return {'messages': messages}, getattr(error, 'code', 405)


@api.errorhandler
def custom_error_handler(error):
    log_error_message(error)
    messages = get_error_messages(repr(error), repr(error))

    return {'messages': messages}, getattr(error, 'code', 500)
