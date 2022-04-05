from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from gevent.pywsgi import WSGIServer

# creating the flask app
app = Flask(__name__)

# creating an API object
api = Api(app)

# Import all class in api
from rest.api import *


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/api')


# driver function
if __name__ == '__main__':
	http_server = WSGIServer(('127.0.0.1', 5050), app)
	http_server.serve_forever()

