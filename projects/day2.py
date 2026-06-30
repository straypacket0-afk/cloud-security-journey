# challenge 1: print numbers from 1-20
# for num in range(1, 21):
    # print(num)
# number = 0
# while number < 20:
    # number += 1
    # print(number)
# challenge 2: print only even numbers from 1-30
# for num in range(1, 31):
    # if num % 2 == 0:
        # print(num)
# challenge 3: print only odd numbers
# for num in range(1, 31):
    # if num % 2 == 1:
        # print(num)
# challenge 4: print every letter in the variable - word
# word = "keyboard"
# for w in word:
    # print(w)
# challenge 5: countdown 10-1 and blast off
# countd = 11
# while countd > 1:
#     countd -= 1
#     print(countd)
# print("Blast off!")
# this one took quite some time lol..
# challenge 6: print the multiplication table of 7
# for num in range(1, 13):
    # print(f"7 x {num} = {7*num}")
# this one took me less effort!! suprisingly1
# challenge 7: print squares
# for num in range(1, 16):
    # print(f"{num} squared is {num*num}")
# ey yo!! i think knowing how this works makes it easier at every step!
# challenge 8: print cubes from 1-10
# for num in range(1, 11):
    # print(f"{num} = {num*num*num}")
# challenge 9: find the sum of 1-100
# total = 0
# for i in range(1, 101):
    # total += i
# print(total)
# cheated.
# find the sum of only even numbers from 1-100
# total = 0
# for i in range(1, 101):
    # if i % 2 == 0:
        # total += i
# print(total)
# challenge 11: multiply numbers from 1-5
# total = 1
# for i in range(1, 6):
#     total *= i
# print(total)
# challenge 12: count how many letters in the variable without using len()
# word = "computer"
# total = 0
# for words in word:
#     total += 1
# print(total)
# easy
# challenge 13: count vowels in variable
# word = "education"
# vowel = ["i","e","o","a","u"]
# total = 0
# for char in word:
#     if char in vowel:
#         total += 1
#         print(char)
# print(total)
# okay..
# challenge 14: count how many times a appears in banana
# total = 0
# for a in "banana":
#     if a == "a":
#         total += 1
# print(total)
# challenge 15: reverse a word using loops no slicing
word = "python"
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

