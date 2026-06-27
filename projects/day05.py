import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
 
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for l in range(1, nr_letters+1):
    let = random.choice(letters)
    password.append(let)
for n in range(1, nr_numbers+1):
    num = random.choice(numbers)
    password.append(num)
for s in range(1, nr_letters+1):
    sym = random.choice(symbols)
    password.append(sym)
random.shuffle(password)
print(password)
result = "".join(map(str, password))
print(result)