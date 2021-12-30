import json
from datetime import datetime
filename = datetime.today().strftime('%Y-%m')
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
