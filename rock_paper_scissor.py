import random
user_wins =0
computer_wins = 0

options = ["rock" , "pepar","scissor"]
while True:
    user_input= input("Type Rock/Pepar/Scissor q for quit :").lower()
    if user_input == "q":
     break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer = options[random_number]
    print("computer pick" , computer + ".")

    if user_input == "rock" and computer == "scissor":
       print("you win")
       user_wins+=1

    elif user_input == "pepar" and computer == "rock":
       print("you win")
       user_wins+=1

    elif user_input == "scissor" and computer == "pepar":
       print("you win")
       user_wins+=1
    else:
       print("you lost")
       computer_wins+=1
    print("you won" , user_wins, "times")
print("the computer won" , computer_wins ,"times")




