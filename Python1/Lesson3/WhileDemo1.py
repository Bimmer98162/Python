import random

i = 1
correctNum = random.randint(1, 10)
while (i <= 3):
    x = int(input("x = "))
    i += 1
    if (x == correctNum):
        print("Correct! Congratulations!")
        break
    elif (x < correctNum):
        print(f"Incorrect! Your number is LOWER! You have {4 - i} chances left.")
    elif (x > correctNum):
        print(f"Incorrect! Your number is HIGHER! You have {4 - i} chances left.")
