import os
import logging
import pytest

from flask import current_app
from flask_testing import TestCase
from pyannotate_runtime import collect_types

from {{cookiecutter.app_name}}.app import create_app

logging.disable(logging.CRITICAL)


def pytest_addoption(parser):
    parser.addoption(
        '--annotate',
        action='store_true',
        help='generate pyannotate files'
    )

@pytest.fixture
def annotate(request):
    return request.config.getoption("--annotate")

class AppTestCase(TestCase):
    """Allows `--annotate` flag to create type_info"""

    def create_app(self):
        os.environ['FLASK_ENV'] = 'testing'
        app = create_app('testing')
        # pylint: disable=E1101
        app.config['ANNOTATE'] = annotate
        return app

    def setUp(self):
        super(AppTestCase, self).setUp()
        if current_app.config['ANNOTATE']:
            if not os.path.exists('type_info'):
                os.makedirs('type_info')
            collect_types.init_types_collection()

    def tearDown(self):
        super(AppTestCase, self).tearDown()
        if current_app.config['ANNOTATE']:
            collect_types.dump_stats(
                'type_info/{}.json'.format(type(self).__name__))

    def run(self, result=None):
        if current_app.config['ANNOTATE']:
            # run and collect annotations
            with collect_types.collect():
                super(AppTestCase, self).run(result)
        else:
            super(AppTestCase, self).run(result)
