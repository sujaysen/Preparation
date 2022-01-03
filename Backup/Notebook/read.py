import json
from datetime import datetime

filename = input("Enter the filename (mm-yyyy) : ")
if not filename:
    filename = datetime.today().strftime('%m-%Y')

try:
    fp = open(filename,"r")
    total_expense = 0
    total_income = 0

    for r in fp.readlines():
        data = json.loads(r)
        if "expense" in data:
          total_expense = total_expense + data["expense"]
        if "income" in data:
          total_income = total_income + float(data["income"])

    print("Total Expense = ",total_expense)
    print("Total Income = ",total_income)
    fp.close()

    fpp = open(filename,"r")
    flag = input("Do you want to know expense and income of some day(1 for yes ) : ")
    if flag:
        flag = 1
    else:
        flag = 0

    if flag:
        date = input("Enter the date(mm) : ")
        for res in fpp.readlines():
            data = json.loads(res)
            if data["date"] == date:
                print(data)
                print("Expense = ",data["expense"])
                print("Income = ",data["income"])
    fpp.close()
except:
    print("Enter the correct filename")

