# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print(
        f"The computer choosed {computer_choice}\n"
        f"You choosed {user_choice}\n"
)
# Run Conditionals
if ((user_choice=="r" and computer_choice=="p") or (user_choice=="p" and computer_choice=="s") or (user_choice=="s" and computer_choice=="r")):
    print("The computer won.")
elif ((user_choice=="p" and computer_choice=="r") or (user_choice=="r" and computer_choice=="s") or (user_choice=="s" and computer_choice=="p")):    
    print("You won.")
else:
    print("Its a tie!")
