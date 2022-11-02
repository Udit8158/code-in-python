import random

# Variables
randomNumber = random.randint(0, 100)
count = 0

# Main logic
while True:
    inputNumber = input("Enter a random number between 0 to 100-> ")
    try:
        inputNumber = int(inputNumber)
    except:
        print("Please Enter a valid number !!!!!!!")
        continue
    if (inputNumber > randomNumber):
        count += 1
        print("Enter a small number")
    elif (inputNumber < randomNumber):
        count += 1
        print("Enter a larger number")
    elif (inputNumber == randomNumber):
        count += 1
        print(f"You gussed the number correctly in {count} turns !!!")
        break
