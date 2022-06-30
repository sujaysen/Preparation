    ###### Bell Numbers #######
"""
Given a set of n elements, find number of ways of partitioning it. 
Suppose n = 2 then total number of ways is 2 [{{1},{2}},{1,2}]
Suppose n = 3 then all posibilities are
[{{1},{2},{3},}
{{1},{2,3}},
{{2},{1,3}},
{{3},{1,2}},
{1,2,3}]
Total number of ways = 5
Bell triangle :
1                  >> dp[0][0] = 1
1 2                >> dp[1][1] = dp[1][0] + dp[0][0] = 1 + 1 = 2
2 3 5              >> dp[2][2] = dp[2][1] + dp[1][1] = 3 + 2 = 5
5 7 10 15     
15 20 27 37 52

dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

Time complexity = O(n*n)
Space complexity = O(n*n)

"""
def bell_number(number):
	dp = [[0 for i in range(number+1)] for j in range(number+1)]
	return dp

while True:
	number = int(input("Enter the given number : ") or -1)
	if number == -1:
		print("Quit!!")
		quit()
	result = bell_number(number)
	print("Total number of partitions of {} is {}".format(number,result))
