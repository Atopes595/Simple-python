# Input your age
age = int(input("Enter your age:"))
if age <= 19:
	print ("You qualify for student discounts.")
elif 20<= age <= 54:
	print ("You qualify for no discounts.")
else:
	print ("You qualify for senior dicounts.")

