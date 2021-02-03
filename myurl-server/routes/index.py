
from flask import Blueprint
from controllers.test import Test

route = Blueprint('index', __name__, url_prefix='/')

@route.route('/tr')
def index():
	return Test.get_students()