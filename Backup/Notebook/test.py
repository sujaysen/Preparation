import json
from datetime import datetime

filename = input("Enter the filename(dd-mm) : ")
if not filename:
    filename = datetime.today().strftime('%d-%m')
file_p = open(filename,"a+")
data = {}

while(int(input("Do you want to write? 1 for yes else 0 : "))):
  field = input("Enter the field name : ")
  value = input("Enter the value : ")
  data[field] = value

expense = 0

for res in data:
  expense = expense + float(data[res])

data["expense"] = expense
data["income"] = float(input("Enter income : "))

day = input("Enter date : ")
if not day:
  day = datetime.today().strftime('%d') 
data["date"] = day

try:
    file_p.writelines(json.dumps(data)+"\n")
    file_p.close()
    print("Written Successfully!!!!")
except:
    print("Error Occoured..")
