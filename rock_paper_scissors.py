import random

print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"]

while True:

    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))

            if 1 <= choice <= 3:
                break
            else:
                print("Please enter a valid choice (1-3).")

        except ValueError:
            print("Please enter a valid number.")

   
    user_choice = choices[choice - 1]

    print("\nUser choice is:", user_choice)
    print("Now it's Computer's Turn...")

    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)
    print(user_choice, "vs", computer_choice)

    if choice == comp_choice:
        print("<== It's a Tie! ==>")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("<== User Wins! ==>")

    else:
        print("<== Computer Wins! ==>")

    while True:
        ans = input("\nDo you want to play again? (Yes/No): ").lower()

        if ans in ['yes', 'no']:
            break

        print("Please enter Y or N.")

    if ans == 'n':
        break

    print()

print("\nThanks for playing!")
