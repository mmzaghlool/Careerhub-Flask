from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .user import *
from .Chat import *