from flask import Flask

app = Flask(__name__)

from app import routes  # This imports routes and connects them with the app
