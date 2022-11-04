"""
Create Blurprint for main
"""
from flask import Blueprint

bp = Blueprint('main', __name__)

#pylint: disable=wrong-import-position, cyclic-import
from app.main import routes
#pylint: enable=wrong-import-position, cyclic-import
