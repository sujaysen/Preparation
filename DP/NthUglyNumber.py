     #### Nth ugly number  #####
"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … 
Given a number n, the task is to find n’th Ugly number.

Time complexity = O(n)
Space complexity = O(n)

"""

def nthUgly(num):
	ugly = [0]*num
	ugly[0] = 1
	i2 = i3 = i5 = 0

	next_mul_2 = ugly[i2]*2
	next_mul_3 = ugly[i3]*3
	next_mul_5 = ugly[i5]*5

	for i in range(1,num):
		ugly_num = min(min(next_mul_2,next_mul_3),next_mul_5)
		ugly[i] = ugly_num

		if ugly_num == next_mul_2:
			i2 +=1
			next_mul_2 = ugly[i2]*2

		if ugly_num == next_mul_3:
			i3 +=1
			next_mul_3 = ugly[i3]*3

		if ugly_num == next_mul_5:
			i5 +=1
			next_mul_5 = ugly[i5]*5

	return ugly[-1]

while True:
	num = int(input("Enter a number : ") or -1)
	if num == -1:
		print("Quit")
		quit()
	resp = nthUgly(num)
	print("Nth ugly number is ",resp)
