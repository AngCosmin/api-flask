from flask import Blueprint

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    return 'Hello World'


