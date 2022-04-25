if open_price:
	execute("buy on open price")
if current_price >= desired_price:
	execute("sell on that price")
elif current_price <= stoploss:
	execute()
