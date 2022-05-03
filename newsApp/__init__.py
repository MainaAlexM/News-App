from flask import Flask
from newsApp import error

app = Flask(__name__)

from newsApp import views
