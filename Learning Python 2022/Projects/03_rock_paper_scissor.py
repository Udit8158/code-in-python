import random

print("Welcome to Rock-Paper-Scissors Game")
options = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0
win = None
chosen_round = int(input("Choose Number of round in digit you want to play with computer : "))
round = 0

while round < chosen_round:
    user_input = input("Enter Rock/Paper/Scissor as options or Q for quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Please enter valid options")
        continue
    else:
        random_number = random.randint(0, 2)
        computer_input = options[random_number].lower()
        print(f"You choose -> {user_input} and Computer choose -> {computer_input}")
        if user_input == computer_input:
            print("Game Draw")
            round += 1
        elif user_input == "rock" and computer_input == "paper":
            print("Computer Won")
            computer_score += 1
            round += 1
        elif user_input == "rock" and computer_input == "scissor":
            print("You Won")
            user_score += 1
            round += 1
        elif user_input == "paper" and computer_input == "scissor":
            print("Computer Won")
            computer_score += 1
            round += 1
        elif user_input == "paper" and computer_input == "rock":
            print("You Won")
            user_score += 1
            round += 1
        elif user_input == "scissor" and computer_input == "paper":
            print("You Won")
            user_score += 1
            round += 1
        elif user_input == "scissor" and computer_input == "rock":
            print("Computer Won")
            computer_score += 1
            round += 1

if user_score > computer_score:
    win = "User"
elif user_score < computer_score:
    win = "Computer"
else:
    win = "Both"
print(f"Your Score -> {user_score} and Computer Score -> {computer_score}, so {win} won......")
