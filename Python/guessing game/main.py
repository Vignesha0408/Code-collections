/*4) Develop a C program which demonstrates interprocess communication 
between a reader process and a writer process. Use mkfifo, open, read, write 
and close APIs in your program. 
SOURCE CODE:  
WRITERS PROCESS: 
#include<stdio.h> 
#include<fcntl.h> 
#include<sys/types.h> 
#include<sys/stat.h> 
#include<unistd.h> 
int main() 
{ 
    int fd; 
    char buf[1024]; 
    char *myfifo="'/myfifo"; 
    mkfifo(myfifo,0666); 
    printf("Run readers process to read the FIFO file\n"); 
    fd=open(myfifo,O_WRONLY); 
    write(fd,"Hii",sizeof("Hi")); 
    close(fd); 
    unlink(myfifo); 
    return 0; 
} 
 
WRITERS PROCESS: 
#include<stdio.h> 
#include<fcntl.h> 
#include<sys/types.h> 
#include<sys/stat.h> 
#include<unistd.h> 
#define MAX_BUF 1024 
int main() { 
int fd; 
char *myfifo="./myfifo"; 
char buf[MAX_BUF]; 
fd=open(myfifo,O_RDONLY); 
read(fd,buf,MAX_BUF); 
printf("Write: %s\n",buf); 
return 0; 
}*/


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
