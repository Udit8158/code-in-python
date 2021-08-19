import random

lowRange = 30
highRange = 40
n = random.randint(lowRange, highRange)
turnsToFind = 5
e = turnsToFind-1

print(
    f"Try to guess a number which in hidden,but the number is in range between {lowRange} to {highRange}")
print(f"You have only {turnsToFind} turns")
while True:
    g = int(input("Enter your guess:"))
    if g > highRange or g < lowRange:
        print("Your number is not in givven range")
        break
    if e <= 0:
        print("Your turn is over")
        break
    if g == n:
        print("You guess sucessfully")
        break
    else:
        print(f"Try again,you entered a wrong guess\nYou left {e} turns")
        e = e-1
        continue
print(f"The unknown number was={n}")
