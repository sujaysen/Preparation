class Pet:
	def __init__(self,name,age):
		self.name = name
		self.age = age

class Cat(Pet):
	def __init__(self,name,age):
		super().__init__(name,age)

def Main():
	thepet = Pet("pet",1)
	jess = Cat("jess",3)
	print("is jess a cat ?",str(isinstance(jess,Pet)))

if __name__=='__main__':
	Main()
