from {{cookiecutter.app_name}} import __version__
from {{cookiecutter.app_name}}.tests.conftest import AppTestCase


class HealthcheckTestCase(AppTestCase):
    url = '{{cookiecutter.app_name}}/version'

    def test_healthcheck_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_healthcheck_url_with_slash(self):
        resp = self.client.get(self.url + '/')
        self.assertEqual(resp.status_code, 404)

    def test_healthcheck_version(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.json['version'], __version__)

    def test_healthcheck_docs(self):
        resp = self.client.get(self.url)
        self.assertIsInstance(resp.json['docs'], list)
