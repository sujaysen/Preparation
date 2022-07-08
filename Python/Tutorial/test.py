import threading
import time

def insert_doc(es,index,idd,body):
	time.sleep(2)
	print(es)
	print(index)
	print(idd)
	print(body)

if __name__ == '__main__':
	es = "es"
	voice_idx = "voice"
	string = "just test"
	string_original = "just test"
	search_term = "just"
	resp = 0
	date = "date"
	th = threading.Thread(target=insert_doc, args=(es,voice_idx,string.replace(" ","").lower(),{"istring":string_original,"ostring":search_term,"resp":0,"timestamp":date}
), kwargs={})
	th.start()
	print("Got response")
	
