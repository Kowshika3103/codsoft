import random
user_action=input("enter a choice(rock,paper,scissors):")
possible_action=["rock","paper","scissors"]
computer_action=random.choice(possible_action)
print(f"\n You chose{user_action},computer chose{computer_action}.\n")
if user_action==computer_action:
    print(f"Both players selected{user_action},it's a tie!")
elif user_action=="rock":
    if computer_action=="scissors":
        print("Rock smashes scissors!You win!")
    else:
        print("Paper covers rock!You lose.")
elif user_action=="paper":
    if computer_action=="rock":
        print("Paper covers rock!You win!")
    else:
        print("Scissors cuts pare!You lose")
elif user_action=="scissors":
    if computer_action=="paper":
        printf("Scissors cuts paper!You win!")
    else:
        print("Rock smashes scissors!You lose.")
        
            
