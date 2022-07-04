    ####    Minimum number of Coins    ####
"""
Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N.

Input: N = 43
Output: 20 20 2 1
Explaination: 
Minimum number of coins and notes needed 
to make 43 is 4

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

"""

def minPartition(n):
	pass


while True:
	n = int(input("Enter the number : ") or -1)
	if n == -1:
		print("Quit!")
		quit()
	resp = minPartition(n)
	print("Minimum number of coins ",resp)
