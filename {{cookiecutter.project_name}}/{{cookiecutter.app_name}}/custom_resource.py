from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from {{cookiecutter.app_name}}.custom_error_message import custom_abort


class CustomResource(Resource):
    ''' This class overrides the validate_payload method in order to
        match the validation  error message format conventions
        at Equinox. All resources should extend from this class
        instead of main Resource class from flask_restplus '''

    # Override validate_payload method from Resource class
    def validate_payload(self, func):
        try:
            super().validate_payload(func)
        except BadRequest as e:
            if hasattr(e, 'data'):
                friendly_message = ''
                for field, error in e.data.get('errors').items():
                    friendly_message = error
                    break   # just need to send first validation error
                custom_abort(
                    400,
                    e.data.get('message'),
                    friendly_message=friendly_message,
                    message_type='Validation'
                )
            else:
                custom_abort(
                    400,
                    e.description,
                    friendly_message=e.description,
                    message_type='Validation'
                )
