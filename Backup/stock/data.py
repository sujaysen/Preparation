import requests
import json
from pprint import pprint

token = "61c46a8c27d327.05895362"
symbol = "JUSTDIAL"
url = "https://eodhistoricaldata.com/api/eod/JUSTDIAL.NSE?api_token=61c46a8c27d327.05895362" 
r = requests.get(url)
for i in r.text:
  print(i)
  print(type(i))
  print("************************")
