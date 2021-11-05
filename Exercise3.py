import random
a=random.randint(0,100)
chosen_one=int(input("Give me a number"))
while a != chosen_one:
    if chosen_one>a:
        print("decrease your number")
    else:
        print("increase your number")
    chosen_one=int(input("Give me a number"))
print("Congratulations !!! You guess the number correctly")