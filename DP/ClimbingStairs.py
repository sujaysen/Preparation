       ###### Climbing Stairs dynamic program  ######
"""
There are n stairs, a person standing at the bottom wants to reach the top. 
The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top

t(0) = 1
t(1) = 1
t(2) = t(0) + t(1) = 2
t(n) = t(n-1) + t(n-2)

"""
def climbing_stairs(n):
  dp = [0]*(n+1)
  dp[0] = 1
  dp[1] = 1
  for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

n = int(input("Enter the value of n : "))
print("Total Number of Ways : ",climbing_stairs(n))
