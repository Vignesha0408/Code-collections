#Rock-Paper-Scissors
import math 
import random
print("Instruction ")
print("press r for Rock ")
print("press p for Paper ")
print("press s for Scissors ")
options = ["Rock","Paper","Scissors"]
comupter_choice = random.choice(options)
user_choice = input("choose your option\n")
if user_choice == "r" :
    user_choose = "Rock"
if user_choice == "p" :
    user_choose = "Paper"
if user_choice == "s" :
    user_choose = "Scissors"
print("You choose",user_choose)
print("Computer choose",comupter_choice)

if user_choose == "Rock" and comupter_choice =="Rock":
    print("match tie")
elif user_choose == "Rock" and comupter_choice =="Paper":
    print("you loose the match")
elif user_choose == "Rock" and comupter_choice =="Scissors":
    print("you won the match")



elif user_choose == "Paper" and comupter_choice =="Rock":
    print("you won the match")
elif user_choose == "Paper" and comupter_choice =="Paper":
    print("match tie")
elif user_choose == "Paper" and comupter_choice =="Scissors":
    print("you loose the match")
    



elif user_choose == "Scissors" and comupter_choice =="Rock":
    print("you loose the match")
elif user_choose == "Scissors" and comupter_choice =="Paper":
    print("you won the match")
elif user_choose == "Scissors" and comupter_choice =="Scissors":
    print("match tie")

    
 
    