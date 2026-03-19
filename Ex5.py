def factorial_while(n):
	#use while
	result  = 1
	i = 1
	while i<=n:
		result *= i
		i += 1
	return result

def factorial_for(n):
	#use for
	result = i
	for i in range(1, n+1):
		result *= i
	return result
#input the number
num = int(input("Enter a number to find its factorial:"))
print ("Result using while loop {0}".format(factorial_while(num)))
print ("Result using for loop{0}".format(factorial_for(num)))

