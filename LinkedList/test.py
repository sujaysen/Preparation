from main import LinkedList,Node

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.append(0)
llist.append(1)
llist.append(0)
llist.printList()
llist.delete(2)
print("After delete : ")
llist.printList()
print("Total Node = ",llist.countNode())
print("Occurences = ",llist.nouberOfOccur(0))
if llist.search(10):
	print("Exist!")
else:
	print("Not Exist")

llist.checkPalindrome()

