import hashlib

while True:

  password = input("Please provide a password to test hashing it:\n")
  print(hashlib.md5(password.encode()).hexdigest())

  choice = input(
    "Would you like to try a different password? Type Y for yes or N for no: ")

  if choice == 'n' or choice == 'N':
    break
