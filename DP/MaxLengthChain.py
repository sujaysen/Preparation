    ####    Max length chain    ####
"""
You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. 
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
You have to find the longest chain which can be formed from the given set of pairs. 

Input:
N = 5
P[] = {5  24 , 39 60 , 15 28 , 27 40 , 50 90}
Output: 3
Explanation: The given pairs are { {5, 24}, {39, 60},
{15, 28}, {27, 40}, {50, 90} },the longest chain that
can be formed is of length 3, and the chain is
{{5, 24}, {27, 40}, {50, 90}}

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N)

"""

def maxChainLen(pairs,n):
	pass


while True:
	n = int(input("Enter the number of pairs : ") or -1)
	if n == -1:
		print("Quit!")
		quit()
	pairs = [item for item in input("Enter pairs : ").split()]
	resp = maxChainLen(pairs,n)
	print("Maximum chain length is ",resp)
