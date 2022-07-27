 #####    Minimum Operations  #####
"""
Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:
Double the number
Add one to the number
Input:
N = 8
Output: 4
Explanation: 0 + 1 = 1, 1 + 1 = 2,
2 * 2 = 4, 4 * 2 = 8

Expected Time complexity = O(logn)

"""

def min_operation_dp(n):
	if n<= 1:
		return n
	dp = [0]*(n+1)
	dp[1] = 1
	dp[2] = 2
	for i in range(3,n+1):
		if i%2 == 0:
			dp[i] = dp[i//2] + 1
		else:
			dp[i] = dp[i-1] + 1
	return dp[n]

def min_operation_itr(n):
	min_count = 0
	while(n>0):
		if n%2 == 1:
			n = n-1
			min_count+=1
		elif n%2 == 0 and n>=2:
			n = n//2
			min_count+=1
	return min_count

while True:
	n = int(input("Enter the given number : ") or -1)
	if n == -1:
		print("Quit!")
		quit()
	resp = min_operation_dp(n)
	print("Minimum number of operation to reach {} is {}".format(n,resp))
	res = min_operation_itr(n)
	print("Minimum number of operation to reach {} is {}".format(n,res))
	
