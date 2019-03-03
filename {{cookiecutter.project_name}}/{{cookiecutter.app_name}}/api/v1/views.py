from flask_restplus import fields
from flask import request

from {{cookiecutter.app_name}}.custom_resource import CustomResource as Resource
from {{cookiecutter.app_name}}.api import ns
from {{cookiecutter.app_name}}.custom_error_message import custom_abort

model_find_lead = ns.model('find_lead', {
    "firstName": fields.String(required=False),
    "lastName": fields.String(required=False),
    "emailAddress": fields.String(required=False),
    "phoneNumber": fields.String(required=False),
    'facilityID': fields.String(required=False),
    "tokenID": fields.String(required=True),
    'dataSourceID': fields.String(required=False),
    'outreachCode': fields.String(required=False),
})


@ns.route('/lead', methods=['GET'])
class Lead(Resource):

    @ns.expect(model_find_lead, validate=True)
    def get(self):
        """
        Get {{cookiecutter.app_name}} from Engage
        """
        data = request.json
        if not data:
            custom_abort(
                400, 'Empty input data', 'Empty input data'
            )

        return {'lead': request.json}, 200
