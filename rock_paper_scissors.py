import random
options=["rock","paper","scissors"]
user_choice= input("Enter your choice : ")
computer_choice= random.choice(options)
print("Computer chose ")
print(computer_choice)
if user_choice == computer_choice:
    print("It's a tie!!")
elif user_choice=="scissors" and computer_choice=="paper" :
    print("Yay!! You won :D")
elif user_choice=="rock" and computer_choice=="scissors" :
    print("Yay!! You won :D")
elif user_choice=="paper" and computer_choice=="rock" :
    print("Yay!! You won :D")
elif user_choice=="scissors" and computer_choice=="rock" :
    print("Oh noo!! You lost :(")
elif user_choice=="rock" and computer_choice=="paper" :
    print("Oh noo!! You lost :(")
elif user_choice=="paper" and computer_choice=="scissors" :
    print("Oh noo!! You lost :(")  


