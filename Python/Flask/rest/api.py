from flask import Flask, jsonify, request
from flask_restful import Resource, Api

class Hello(Resource):

	# corresponds to the GET request.
	def get(self):
		#data = request.args.get("data")
		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201

