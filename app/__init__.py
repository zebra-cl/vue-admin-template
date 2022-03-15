import logging
import os

from flask import Flask, send_file
from flask_appbuilder import AppBuilder, SQLA, expose, IndexView

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__, static_folder='../dist/static')

app.config.from_object("config")
db = SQLA(app)


class _IndexView(IndexView):
  @expose("/")
  def index(self):
    return send_file(os.path.join(os.path.dirname(__file__), '../dist/index.html'))


appbuilder = AppBuilder(app, db.session, indexview=_IndexView)

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
