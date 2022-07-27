import threading
import time

def hi():
	i = 0
	while True:
		print("Hi-",i)
		i+=1
		time.sleep(1)

def hello():
	i = 0
	while True:
		print("hello-",i)
		i+=1
		time.sleep(1)

def hellohi():
	i = 0
	for i in range(10):
		print("hellohi-",i)
		i+=1
		time.sleep(1)


if __name__=='__main__':
	try:
		t1 = threading.Thread(target=hi)
		t2 = threading.Thread(target=hello)
		t3 = threading.Thread(target=hellohi)

		t3.start()
		t3.join()
		t1.start()
		t2.start()

		#t1.join()
		i = 0
		while True:
			print("sujay-",i)
			i+=1
			time.sleep(1)

		print("Execution end!")
	except KeyboardInterrupt:
		print("Exit")
	else:
		print("Error")
		
