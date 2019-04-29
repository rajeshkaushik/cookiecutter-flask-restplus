import logging

{% if cookiecutter.slackclient == 'y' %}
class SlackLogHandler(logging.Handler):

    def __init__(self, token, channel):
        super().__init__()
        self.token = token
        self.channel = channel

        from slackclient import SlackClient

        self.client = SlackClient(token)

    def emit(self, record):
        self.client.api_call(
            'chat.postMessage',
            channel=self.channel,
            text=self.format(record)
        )
{% endif %}


def get_custom_formatter(config):
    return logging.Formatter(config.LOG_FORMAT)


{% if cookiecutter.slackclient == 'y' %}
def get_slack_error_handler(config):
    formatter = get_custom_formatter(config)
    handler = SlackLogHandler(config.SLACK_TOKEN, config.SLACK_CHANNEL)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    return handler
{% endif %}


def format_headers(headers, excludes=[]):
    """Returns a dictionary after excluding blacklisted headers"""
    _h = {}
    for k, v in headers.items():
        if k not in excludes:
            _h[k] = v
    return _h
