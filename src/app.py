import pymongo
from flask import Flask, render_template, request, jsonify, make_response
from utils.converters import RegexConverter

app = Flask(__name__)
app.secret_key = 'movidesk'
app.url_map.converters['regex'] = RegexConverter

from views import *

# testing some things

if __name__ == '__main__':
    app.run()
