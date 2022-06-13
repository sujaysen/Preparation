import cryptocode
string = "share price of bank of india bangalore"
encoded = cryptocode.encrypt(string,"1")
print(encoded)
## And then to decode it:
decoded = cryptocode.decrypt(encoded, "1")
print(decoded)
quit()
d = {}
phrase = "bank of india"
res = []
if string.find(phrase) != -1:
	res = [w for w in string.split(phrase) if w != '']
	if len(res) >1:
		d["first"] = res[0]
		d["last"] = res[1]
	elif len(res) == 1:
		d["first"] = res[0]
		d["last"] = ""
	else:
		d["first"] = ""
		d["last"] = ""
		
	d["phrase"] = phrase

print(res)
print(d)
print((d["first"]+" "+d["phrase"]+" "+d["last"]).strip())

