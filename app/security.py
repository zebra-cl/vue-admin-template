from flask import Response
from flask_appbuilder.api import expose, safe
from flask_appbuilder.security.api import SecurityApi
from flask_jwt_extended import jwt_required, current_user
from marshmallow import Schema, fields

from app.utils import make_json_resp


class SecurityApiEx(SecurityApi):
    resource_name = 'security'
    version = "v2"

    @expose("/login", methods=["POST"])
    def login(self) -> Response:
        resp = super().login()
        if 'access_token' in resp.json:
            return make_json_resp({'token': resp.json['access_token']})
        else:
            return resp

    @expose("/refresh", methods=["POST"])
    def refresh(self) -> Response:
        resp = super().refresh()
        if 'access_token' in resp.json:
            return make_json_resp({'token': resp.json['access_token']})
        else:
            return resp

    @expose("/userinfo", methods=["GET"])
    @jwt_required
    @safe
    def userinfo(self):
        class _Schema(Schema):
            name = fields.String(attribute='username')
            avatar = fields.String(
                default='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif')
            roles = fields.List(fields.String())

        return make_json_resp(_Schema().dump(current_user))
