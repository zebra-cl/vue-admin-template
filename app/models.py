from flask import current_app
from flask_appbuilder import Model, SQLA
from sqlalchemy import *
from sqlalchemy.orm import relationship
from werkzeug.local import LocalProxy

db: SQLA = LocalProxy(lambda: current_app.extensions['sqlalchemy'].db)

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
