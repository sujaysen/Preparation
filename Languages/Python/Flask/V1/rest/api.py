from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from V1.handler.test import display

class Hello(Resource):

	# corresponds to the GET request.
	def get(self):
		#data = request.args.get("data")
		data = display()
		print(data)
		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201

