""" Settings added as specified in following link
http://docs.gunicorn.org/en/stable/settings.html
"""

from {{cookiecutter.app_name}} import config as conf
import multiprocessing

# log to stdout.
accesslog = '-'

bind = '{}:{}'.format(conf.HOST, conf.PORT)
# not quite right, using the instance cpu count, not ECS cpu count
# need a better way to determine this
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4
threads = 2
