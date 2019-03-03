from flask_restplus import Namespace

ns = Namespace('Lead', path='/')


from {{cookiecutter.app_name}}.api.v1 import views  # noqa
