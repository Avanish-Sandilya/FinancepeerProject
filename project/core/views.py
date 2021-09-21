from flask import render_template, request, Blueprint, flash
import re
from project import db


core = Blueprint('core', __name__)

@core.route('/', methods=['GET'])
def index():
    return render_template("home.html")
