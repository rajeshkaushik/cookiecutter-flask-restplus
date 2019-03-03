import json
import os
from flask import current_app
from {{cookiecutter.app_name}}.tests.conftest import AppTestCase

class LeadMockTestCase(AppTestCase):
    url = '{{cookiecutter.app_name}}/v1/lead'
    update_lead_url = '{{cookiecutter.app_name}}/v1/lead/c78b86e1-5628-441a-bb8b-9d43a03947ec'
    data_find_lead = {
        "facilityID": '115',
        "emailAddress": "testpy@mail.com",
        "firstName": "rajkumar",
        "lastName": "rao",
        "phoneNumber": '123456789',
        "dataSourceID": "e06f96f2-60bd-48cb-81a1-9dfe05bf38eb",
        "tokenID": "e06f96f2-60bd-48cb-81a1-9dfe05bf38eb"
    }

    def setUp(self):
        self.client.environ_base[
            'HTTP_APIKEY'] = '0470e318-5c1e-427e-8119-edff81e23c03'  # set header 'APIKEY' for api auth

    def test_page_not_found(self):
        url = self.url + "123"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        self.assertIn('messages', resp.json)

    def test_method_not_allowed(self):
        url = self.url
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 405)
        self.assertIn('messages', resp.json)

    def test_empty_data_returns_400_status(self):
        data = {}
        resp = self.client.get(
            self.url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(400, resp.status_code)


class ConfigurableAuthorizationTestCase(AppTestCase):
    url = '{{cookiecutter.app_name}}/v1/lead'
    headers = {
        'apikey': '0470e318-5c1e-427e-8119-edff81e23c03',
        'Content-Type': 'application/json'
    }
    data = {
        'tokenID': 'e06f96f2-60bd-48cb-81a1-9dfe05bf38eb'
    }

    def test_api_auth_not_required(self):
        with current_app.app_context():
            current_app.config['APIKEY_REQUIRED'] = False
        self.assertEqual(current_app.config['APIKEY_REQUIRED'], False)
        resp = self.client.get(self.url, data = json.dumps(self.data), headers=self.headers)
        self.assertEqual(resp.status_code, 200)


    def test_api_auth_required(self):
        with current_app.app_context():
            current_app.config['APIKEY_REQUIRED'] = True
            current_app.config['APIKEY'] = '0470e318-5c1e-427e-8119-edff81e23c03'
        self.assertEqual(current_app.config['APIKEY_REQUIRED'], True)
        resp = self.client.get(self.url, data = json.dumps(self.data), headers=self.headers)
        self.assertEqual(resp.status_code, 200)

    def test_api_auth_required_with_invalid_apikey(self):
        with current_app.app_context():
            current_app.config['APIKEY_REQUIRED'] = True
            current_app.config['APIKEY'] = '0470e318-5c1e-427e-8119-edff81e23c03'
        self.assertEqual(current_app.config['APIKEY_REQUIRED'], True)
        headers = self.headers.copy()
        headers['apikey']='random-key'
        resp = self.client.get(self.url, data = json.dumps(self.data), headers=headers)
        self.assertEqual(resp.status_code, 401)
