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
api.add_resource(Autocomplete, '/api')

# driver function
if __name__ == '__main__':
	app.run(debug = True,host='',port='5050')
	#http_server = WSGIServer(('', 5051), app)
	#http_server.serve_forever()

