import csv
import pymongo

stock_array = ["justdial","igl"]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["stock"]

for stock_name in stock_array:
	print("Start Updating the Stock ",stock_name)
	mycol = mydb[stock_name]

	file = open(stock_name+".csv")
	csvreader = csv.reader(file)
	header = []
	header = next(csvreader)


	for row in csvreader:
		try:
			date = row[0]
			buy = float(row[2].replace(",",""))
			today_open = float(row[2].replace(",",""))
			sell = float(row[2].replace(",",""))
			high = float(row[3].replace(",",""))
			low = float(row[4].replace(",",""))
			prev_close = float(row[5].replace(",",""))
			today_close = float(row[6].replace(",",""))
			volume = float(row[11].replace(",",""))

			# condition for Gap up and Gap down
			if today_open > prev_close:
				open_status = "Gap Up"
			else:
				open_status = "Gap Down"

			# For Buying side
			margin = 0.5
			for i in range(4):
				margin_value = margin/100
				stoploss = round(buy - buy*margin_value,1)

				# Condition for profit and loss
				status = "Loss"
				if stoploss < low:
					status = "Profit"

				if status == "Profit":
					profit_margin = round(((high-buy)/buy)*100,2)
				else:
					profit_margin = round(((low-buy)/buy)*100,2)


				idd = date + ":"+str(margin)+":buy"
				doc = {"_id":idd,"date":date,"action":"buy","buy":buy,"stoploss":stoploss,"margin":margin,"profit_margin":profit_margin,"income_status":status,"high":high,"low":low,"prev_close":prev_close,"today_close":today_close,"volume":volume,"opening_status":open_status}
				mycol.update_one({"_id": idd},{"$set": doc},upsert=True)
				#mycol.insert_one(doc)
				margin = margin + 0.5

			# For selling side
			margin = 0.5
			for i in range(4):
				margin_value = margin/100	
				stoploss = round(sell + sell*margin_value,1)
		
				# Condition for profit and loss
				status = "Loss"
				if stoploss > high:
					status = "Profit"

				idd = date + ":"+str(margin)+":sell"
				doc = {"_id":idd,"date":date,"action":"sell","sell":sell,"stoploss":stoploss,"margin":margin,"income_status":status,"high":high,"low":low,"prev_close":prev_close,"today_close":today_close,"volume":volume,"opening_status":open_status}
				mycol.update_one({"_id": idd},{"$set": doc},upsert=True)
				#mycol.insert_one(doc)
				margin = margin + 0.5

		except Exception as e:
			print("Error",e)

