from flask_appbuilder.api import BaseApi, expose, safe
from flask_jwt_extended import jwt_required
from flask_login import current_user
from marshmallow import Schema, fields


class SecurityApiEx(BaseApi):
  resource_name = 'security'
  csrf_exempt = True

  @expose("/userinfo", methods=["GET"])
  @jwt_required
  @safe
  def userinfo(self):
    class _Schema(Schema):
      username = fields.String()
      avatar = fields.String(
        default='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif?imageView2/1/w/80/h/80')
      roles = fields.List(fields.String())

    return _Schema().dump(current_user)

  @expose("/logout", methods=["POST"])
  def logout(self):
    return {}
