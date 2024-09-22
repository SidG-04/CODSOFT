import random
print("Welcome to the Rock, Paper and Scissors Game!")
print("You'll be playing against the computer.")
usr_score = 0
comp_score = 0
i=1
while True:
    print(f"\n\033[1m--- Round {i}--- \033[0m")
    while True:
        usr_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if usr_choice in ['rock', 'paper', 'scissors']:
            break
        print("Invalid choice. Please try again.")
    comp_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"\nYou chose: {usr_choice}")
    print(f"Computer chose: {comp_choice}")
    if usr_choice == comp_choice:
        print("\033[1mIt's a tie!\033[0m")
    elif (
        (usr_choice == 'rock' and comp_choice == 'scissors') or
        (usr_choice == 'scissors' and comp_choice == 'paper') or
        (usr_choice == 'paper' and comp_choice == 'rock')
    ):
        print("\033[1mYou win!\033[0m")
        usr_score += 1
    else:
        print("\033[1mComputer wins!\033[0m")
        comp_score += 1
    print(f"\n\n\033[1mScore :\033[0m\nYou: \033[1m{usr_score}\033[0m\nComputer: \033[1m{comp_score}\033[0m")
    repeat = input("Do you want to play again? (yes/no): ").lower()
    if repeat != 'yes':
        break
    i+=1
print(f"\n\n\033[1mFinal Scores :\033[0m\nYou: \033[1m{usr_score}\033[0m\nComputer: \033[1m{comp_score}\033[0m")
print("\nThanks for playing!")