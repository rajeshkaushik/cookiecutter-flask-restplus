from flask_restplus import abort


def get_error_messages(message, friendly_message, message_type='Error'):
    return [{
        'messageID': None,
        'errorMessage': message,
        'friendlyMessage': friendly_message,
        'messageType': message_type
    }]


def custom_abort(status_code, message, friendly_message, message_type='Error'):
    ''' This function simply calls flask_restplus abort
    with custom error message parameters. This function
    should be used instead of flask_restplus abort function
     to send custom error message as per Equinox conventions '''

    messages = get_error_messages(
        message, friendly_message, message_type
    )
    abort(status_code, messages=messages)
