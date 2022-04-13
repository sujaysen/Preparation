from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from handler import autocomplete

class Autocomplete(Resource):

	# corresponds to the GET request.
	def get(self):
		date = request.args.get("date") or ""
		mobile = request.args.get("mobile") or ""

		if not mobile and not date:
			return jsonify({"message":"Please enter mobile number and date","errorCode":1})
		elif not date:
			return jsonify({"message":"Please enter date also","errorCode":1})
		elif not mobile:
			return jsonify({"message":"Please enter mobile also","errorCode":1})
		else:
			pass

		try:
			autocomplete_result = autocomplete.display(date,mobile)

		except Exception as e:
			return jsonify({"message":"encountered error while fetching results","errorCode":1})

		return jsonify({"errorCode":0,"date": date,"mobile":mobile,"Autocomplete":autocomplete_result})

