pin = "1234"
choice = 0
balance = 10000
print("\n welocme to bank of Godwin\n")
print("insert your atm card\n")
user_pin = input("enter your pin\n")
masked = '*'*len(user_pin)
print(masked)
if user_pin == pin:
	while choice !=4:
		print("***menu***")
		print("1***for balance")
		print("2***for withdrawal")
		print("3***for deposit")
		print("4***to exit")
		choice = int(input("your choice\n"))
		if choice == 1:
			print("your balance is", balance)
			
		elif choice == 2:
			withdrawal = float(input("enter your withdraw amount"))
			net =balance -withdrawal
			print(f"your have withdrawn {withdrawal} and your balance is {net}")
		elif choice == 3:
			deposit = float(input("enter amount you wish to deposit"))
			new = net + deposit
			print(f"your deposited {deposit} and you new balance is {new}")
		elif choice == 4:
			print("goodbye, thank you for banking with us")
else:
	print("enter a valid pin")


weight = float(input("input your weight: "))
unit = input("enter unit: (k or l): ")
if unit == "k":
	weight = weight * 2.204
	unit = "lbs"
elif unit == "l":
	weight = weight / 2.204
	unit ="kgs"
else:
	print(" enter a valid unit")
print(f" your wieght is {weight}{unit}")
