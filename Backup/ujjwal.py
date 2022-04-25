from datetime import date
import time

Policy_holder = input("Enter the name of the policy holder : ") or "sujay"
Agent_name = "ujjwal"

def display_details(name):
	if name == "sujay":
		print("policy name = Jeevan Labh")
		print("Policy_number = 402849906")
		print("Date of Maturity = 30.05.2039")
	elif name == "sulata":
		print("policy name = New Endowment Plan-814")
		print("Policy_number = 135905829")
		print("Date of Maturity = 26.12.2031")
	else:
		pass

if(Policy_holder == "sujay"):
	start_date = '29.08.2018'
	end_date = '30.05.2033'
elif(Policy_holder == "sulata"):
	start_date = '28.12.2016'
	end_date = '26.12.2031'
else:
	pass


today = date.today()
pattern = '%d.%m.%Y'


start_date_epoch = int(time.mktime(time.strptime(start_date, pattern)))
end_date_epoch = int(time.mktime(time.strptime(end_date, pattern)))
today_epoch = time.time()

paid = 0
Unpaid = 0
display_details(Policy_holder)

print("*************** LIST OF PAID INSTALLMENT ****************")
while today_epoch>=start_date_epoch:
    d = time.strftime('%d-%m-%Y', time.localtime(start_date_epoch))
    print("paid-",d)
    start_date_epoch = start_date_epoch + 7889400
    paid += 1

print("*************** LIST OF UNPAID INSTALLMENT ****************")
while end_date_epoch>=start_date_epoch:
    d = time.strftime('%d-%m-%Y', time.localtime(start_date_epoch))
    print("Not Paid - ",d)
    start_date_epoch = start_date_epoch + 7889400
    Unpaid += 1

print("Total number of istallment done = ",paid)
print("Total number of istallment due = ",Unpaid)
