     #### Calculate nth fibonacci number   #####

"""
Given a number n, print n-th Fibonacci Number. 
Fibonacci sequence like
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……
f(0) = 0
f(1) = 2
f(n) = f(n-1) + f(n-2)

Time complexity = O(n)
Space complexity = O(n)

"""

def NthFibonacci(n):
	if n <= 0:
		return 0
	fib = [0]*(n+1)
	fib[0] = 0
	fib[1] = 1
	for i in range(2,n+1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[n]


while True:
	n = int(input("Enter the value of n : ") or -1)
	if n == -1:
		print("Quit")
		quit()
	resp = NthFibonacci(n)
	print("Nth fibonacci number is : ",resp)
