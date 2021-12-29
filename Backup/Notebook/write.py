import json
from datetime import datetime
filename = datetime.today().strftime('%Y-%m')
file_p = open(filename,"a+")
data = {}
data["date"] = datetime.today().strftime('%d')  
while(int(input("Do you want to write? 1 for yes else 0 : "))):
  field = input("Enter the field name : ")
  value = input("Enter the value : ")
  data[field] = value
file_p.writelines(json.dumps(data)+"\n")
file_p.close()
