from main import *

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Inorder traversal : ")
printInorder(root)
print("\nPre Order Traversal : ")
printPreorder(root)
print("\nPost Order Traversal : ")
printPostorder(root)
print()