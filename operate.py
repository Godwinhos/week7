'''
#to calculate user age
user_age = int(input("enter your age: "))
print(f" {user_age} is greater or equal to?",  user_age >= 18)

user_grade = float(input("enter users score: "))
print(f"{user_grade} is greater or equal to?", user_grade >= 70)
'''

'''
pin = 4190
print("welcome to our bank")
user_pin = int(input("enter your pin"))
print(f"is this pin correct?", user_pin == pin)
'''


'''
phone_password =4190
user_password = input("enter user password")
check_password = user_password == phone_password
print(f"user password is, {check_password}")
print(f"{user_password[0]}{'*'*(len(user_password)-1)}")
'''
'''
check_password = "12345"
password = input("enter a valid password\n")
if password == check_password:
	print(f"{password[0]}{'*'*(len(password)-1)}")
	print("successfully logged in")
else:
	print("enter a valid password")
'''

'''
password = input("enter your password: ")
marked = '*'*len(password)
print(marked)
'''

'''
weight = float(input("enter your weight"))
unit = input("enter unit, (k or l)")
if unit == "k":
		weight = weight * 2.204
		unit = "lbs"
elif unit == "l":
		weight = weight / 2.204
		unit = "kgs"
else:
		print("not a valid unit")
print(f" {weight}")

print(5>2 and 10 == 10)
print(not(4 == 4) or 7<2 and 1>0)
print(not(3 == 3))
print(not( 10 > 3))
print(8 >3 and 8>4)
'''

pin = "1234"
choice = 0
balance = 5000
print("\nwelcome to acccess bank\n")
print("insert your atm card\n")
print("enter your four digit pin\n")
user_pin = input("enter your pin\n")
masked = "*"* len(user_pin)
print(masked)
if user_pin == pin:
	while choice !=4:
		print("***menu***\n")
		print("1***balance")
		print("2***withdrawal")
		print("3***deposit")
		print("4***cancel")
		choice = int(input("\nenter your options\n"))
		if choice==1:
			print("your balance is", balance)
		elif choice == 2:
			withdraw = float(input("amount you want to withdraw:\n"))
			net = float(balance) - float(withdraw)
			print(f"you have successfully withdrawn {withdraw} and your balance is {net} \n")
		elif choice == 3:
			deposit = float(input("enter amount you wish to deposit\n"))
			balance +=deposit
			print(balance)
		elif choice == 4:
			print("take your atm and have a great day")
		else:
			print("input a valid input from 1-4")
else:
	print("enter a valid pin")

