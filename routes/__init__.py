from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .user import *
from .Chat import *
from .Courses import *
from .Groups import *
from .Rs import *
from .Notifications import *
from .Search import *
from .ElasticSearch import *
