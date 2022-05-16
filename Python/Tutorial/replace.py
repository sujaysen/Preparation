string = "mujhe i phone chahiye"
dict = {"i phone":"iphone","j w":"jw"}
def replace_substring(string,dict):
	newString = string
	for key,value in dict.items():
		if key in string:
			newString = string.replace(key, value)
	return newString

ans = replace_substring(string,dict)
print(ans)
quit()
for element in list:
    for key,value in dict.items():
        if key in element:
            newElement = element.replace(key, value)
            newDict.append(newElement)
print(newDict)
