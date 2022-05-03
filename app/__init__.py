from flask import Flask
from app import error

app = Flask(__name__)

from app import views
