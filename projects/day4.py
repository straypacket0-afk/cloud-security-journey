import random
numbers = ["0","1","2","3","4","5","6","7","8","9"]
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

longpass = []
print("welcome to password generator!.\n"
"In a word where attckers are always trying to steal your information you need stronger password for your protection")
length = int(input("choose password between 28-35.\n"
"(Don't worry about memorizing the password, we'll help you store and provide it whenever you need it)\n>"))
combined = lower + upper + numbers + symbols
if length > 27 and length < 36:
    for password in range(length):
        let = random.choice(combined) 
        longpass.append(let)
elif length > 35:
    print("too long")
else:
    print("too short")
final = ''.join(longpass)
print(final)

