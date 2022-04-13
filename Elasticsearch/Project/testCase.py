import unittest
import datetime
import requests
import json
import urllib
import time

class RestTests(unittest.TestCase):
	def test_all(self):
		mobile = "9126487714"
		expected_result = -2
		result = -1
		date = Previous_Date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime ('%Y.%m.%d')

		possible_params = [
			{"expected_result":1},
			{"mobile":mobile,"expected_result":1},
			{"date":date,"expected_result":1},
			{"mobile":mobile,"date":date,"expected_result":0},
			{"date":"2021.04.05","expected_result":0,"mobile":mobile}
		]

		for param in possible_params:
			path = urllib.parse.urlencode(param)
			url = "http://localhost:5050/api?"+path
			expected_result = param["expected_result"]

			try:
				print(url)
				time.sleep(4)
				response = requests.get(url).json()
				result = int(response['errorCode'])
			except Exception as e:
				print("Error while call API",e)

			self.assertTrue(result == expected_result)

if __name__ == "__main__":
	unittest.main()

