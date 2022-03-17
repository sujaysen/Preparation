from datetime import date
import time
Policy_holder = input("Enter the name of the policy holder : ") or "sujay"
Agent_name = input("Enter the name of the agent : ") or "ujjwal"

if(Policy_holder == "sujay"):
    if(Agent_name == "ujjwal"):
        start_date = '29.08.2018'
        end_date = '30.05.2033'
    elif(Agent_name == "jagannath"):
        start_date = '25.03.2019'
        end_date = '26.12.2040'
    else:
        print("For sujay available agent name : ujjwal, bapi and jagannath")

elif(Policy_holder == "sulata"):
    start_date = ''
    end_date = ''
else:
    pmode = int(input("if yearly press 1 or if half yearly press 2 or if quarterly press 4 : "))
    start_date = input("Start Date(dd.mm.yyyy) : ")
    end_date = input("End Date(dd.mm.yyyy) : ")

today = date.today()
pattern = '%d.%m.%Y'


start_date_epoch = int(time.mktime(time.strptime(start_date, pattern)))
end_date_epoch = int(time.mktime(time.strptime(end_date, pattern)))
today_epoch = time.time()

paid = 0
Unpaid = 0

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
print("Total amount paid = ",paid*30452)
