import sys  # to use sys.exit to terminate the program

# assumed user balance
user_balance = 1234.55

# assumed user password
user_password = "!234"

welcome_msg = '''
=====================================
==== Welcome to Trusted Bank ATM ====
=====================================
'''

print(welcome_msg)

# get user password and exit if wrong
# pin = input("Enter Password:") # normal input without mask
# . Keep the program running till the user enter exit
# 2.Allow wrong pin for only 3 times then block the account

# use maskpass to replace characters with *
count = 3
while count < 0:
  pin = input("Enter Password again: ")
  if pin != user_password:
    print("Invalid Pin")
    print("Try again")
  count -= 1

  if pin != user_password:
    print("Account blocked")
  # exit
  sys.exit(0)
print(f"\nYour current balance is: ${user_balance}\n")

# show the menu
print("1. Withdraw")
print("2. Deposit")
print("3. Exit")

choice = int(input("Enter 1 or 2: "))
while True:
  if choice == 1:
    amount = float(input("Enter the amount:"))
    if amount <= 0:
      print("Invalid amount")
    elif amount <= user_balance:
      user_balance = user_balance - amount
      print("Take your money")
      print("Your new balance is: ", user_balance)
    else:
      print("Insufficient funds")
  elif choice == 2:
    amount = float(input("Enter the amount:"))
    if amount <= 0:
      print("Invalid amount")
    else:
      user_balance = user_balance + amount
      print("Your new balance is: ", user_balance)
  elif choice == 3:
    print("Thank you for using our ATM")
    break
  
  else:
    print("Invalid Choice!")
