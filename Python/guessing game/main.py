

#you will play the game when you run it
import random
print("\" THE GUESSING GAME\"")
print("\' Let's play game with max\'")
run = True
count=1
while run:
    user_guess = int(input("Enter your guess between 1 to 5\n"))
    computer_guess = int(random.randint(1,5))

    print(f"you choose {user_guess}")
    print(f"max choose {computer_guess}")

    if user_guess == computer_guess:
        print("you won the match")
        break;
    else:
        print("you loose the game\n")
        count=count+1
        y = str(input("do you want to replay the match (press y),press any key to exit\n"))
        if y=="y":
            continue;
        else:
            break;
    
print(f"you played game {count} times")
