import random

#produce random number between 10 and 20.
num = random.randint(10,20)
guess = None

while guess != num:
	guess = int(input("Guess the random number(between 10 and 20):"))
	if guess == num:
		print("You got it!")
	else:
		print("You are wrong~Don't worry")
