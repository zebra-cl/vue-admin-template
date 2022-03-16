from flask import Response
from flask_appbuilder.api import expose, safe
from flask_appbuilder.security.api import SecurityApi
from flask_jwt_extended import jwt_required, current_user
from marshmallow import Schema, fields

from app.utils import make_json_resp


class SecurityApiEx(SecurityApi):
  resource_name = 'security'
  csrf_exempt = True

  @expose("/login/ex", methods=["POST"])
  def login(self) -> Response:
    return make_json_resp(super().login().json)

  @expose("/refresh/ex", methods=["POST"])
  def refresh(self) -> Response:
    return make_json_resp(super().refresh().json)

  @expose("/userinfo", methods=["GET"])
  @jwt_required
  @safe
  def userinfo(self):
    class _Schema(Schema):
      username = fields.String()
      avatar = fields.String(
        default='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif')
      roles = fields.List(fields.String())

    return make_json_resp(_Schema().dump(current_user))
