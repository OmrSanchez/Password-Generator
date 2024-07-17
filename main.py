import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letter_len = len(letters) - 1
sym_len = len(symbols) - 1
num_len = len(numbers) - 1
user_pwd = []
pwd = str(user_pwd).upper()

for i in range(0, (nr_letters)):
  l = letters[random.randint(0, letter_len)]
  user_pwd.append(l)

for i in range(0, nr_symbols):
  s = symbols[random.randint(0, sym_len)]
  user_pwd.append(s)

for i in range(0, (nr_numbers)):
  n = numbers[random.randint(0, num_len)]
  user_pwd.append(n)

print(user_pwd)
random.shuffle(user_pwd)
print(user_pwd)
pwd = ''.join(user_pwd)
print(f'Your password is: {pwd.lower()}')


