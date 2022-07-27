class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next

  def push(self,new_data):
    # allocate node for new data
    new_node = Node(new_data)
    # linked with next node
    new_node.next = self.head
    # make new node as head
    self.head = new_node
    # take O(1) time


  def insertAfter(self,prev_node,new_data):
    if prev_node in None:
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    # take O(1) time

  def append(self,new_data):
    if self.head is None:
      return
    new_node = Node(new_data)
    last = self.head
    while(last.next):
      last = last.next
    last.next = new_node
    # take O(n) time

  def delete(self,key):
    if self.head is None:
      return
    temp = self.head
    if(temp.data == key):
      self.head = temp.next
      temp = None
      return

    while(temp):
      if temp.data == key:
        break
      prev = temp
      temp = temp.next

    if(temp is None):
      return
    prev.next = temp.next
    temp = None

  def countNode(self):
    temp = self.head
    count = 0
    while(temp):
      count = count + 1
      temp = temp.next
    return count

  def nouberOfOccur(self,key):
    count = 0
    temp = self.head
    while(temp):
      if(temp.data == key):
        count = count + 1
      temp = temp.next
    return count

  def search(self,key):
    temp = self.head
    while(temp):
      if(temp.data == key):
        return True
      temp = temp.next
    return False

  def reverseList(self):
    pass

  def isPalindrome(self):
    pass

  def swapData(self):
    pass

  def swapNode(self):
    pass

  def unionList(self):
    pass

  def intersectionList(self):
    pass

  def detectLoop(self):
    pass

  def removeDuplicates(self):
    pass
    






