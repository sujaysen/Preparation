class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.data,end=" ")
		printInorder(root.right)

def printPreorder(root):
	if root:
		print(root.data,end=" ")
		printPreorder(root.left)
		printPreorder(root.right)

def printPostorder(root):
	if root:
		printPostorder(root.left)
		printPostorder(root.right)
		print(root.data,end=" ")