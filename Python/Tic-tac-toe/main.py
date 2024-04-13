
#Documentation 
''' 
to create boart using list
# | | 
#_ _ _
# | | 
#_ _ _
# | | 





to decide win
a=
 |0 ,1 ,2|
 |3 ,4 ,5|
 |6 ,7 ,8|
 
 win user in these conditions
(a[0]=a[1] =a[2]) 
(a[3]=a[4] =a[5])
(a[6]=a[7] =a[8])
(a[0]=a[3] =a[6])
(a[1]=a[4] =a[7])
(a[2]=a[5] =a[8])
(a[0]=a[4] =a[8])
(a[2]=a[4] =a[6])
comparision 3 value at a time not possible 


applying and gate to compare
{
(a[0]==a[1] and a[0]=a[2]  and a[0] == "user1_choice"   ) 
(a[3]==a[4] and a[3]=a[5]  and a[3] == "user1_choice"   )
(a[6]==a[7] and a[6]=a[8]  and a[6] == "user1_choice"   )
(a[0]==a[3] and a[0]=a[6]  and a[0] == "user1_choice"   )
(a[1]==a[4] and a[1]=a[7]  and a[1] == "user1_choice"   )
(a[2]==a[5] and a[2]=a[8]  and a[2] == "user1_choice"   )
(a[0]==a[4] and a[0]=a[8]  and a[0] == "user1_choice"   )
(a[2]==a[4] and a[2]=a[6]  and a[2] == "user1_choice"   ) }else user2 = win


for draw condition if we use 
else:
    print("Match Draw..")
it print's Match draw after each entry of user
we want to know the conditionas for draw,, it can add at last
a=
 |0 ,1 ,2|
 |3 ,4 ,5|
 |6 ,7 ,8|

conditions 
if ther is no winner then it is draw


when all is filled then

if  (a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        break;
















'''



print("Tic-tac-toe game")
x='x';
o='o';

a=[1,2,3,4,5,6,7,8,9]
b=[]
print("The board will look like this, see their positions to play")

#multiline string
print(f'''\n{a[0]}|{a[1]}|{a[2]}\n_ _ _\n{a[3]}|{a[4]}|{a[5]}\n_ _ _\n{a[6]}|{a[7]}|{a[8]}''');
enter=input("Press Enter to continue...")
user1_choice=input("Enter user choice(X/O)..");

if(user1_choice.lower()=='x'):
    user2_choice='o'
elif(user1_choice.lower()=='o'):
    user2_choice='x'
else:
    print("Enter valid choice")


x=0

while(x<=9):
    x+=1;
    
    if(user1_choice.lower() != 'x'and user1_choice.lower()!='o'):
        print("Try again.....")
        break;
    print(f"User1={user1_choice},user2={user2_choice}")
    print(f"User-1..choose {user1_choice}\'s position.....")
    print(f'''{a[0]}|{a[1]}|{a[2]}\n_ _ _\n{a[3]}|{a[4]}|{a[5]}\n_ _ _\n{a[6]}|{a[7]}|{a[8]}''');
    var1=int(input())










    a[var1-1]=user1_choice;
    print(f'''{a[0]}|{a[1]}|{a[2]}\n_ _ _\n{a[3]}|{a[4]}|{a[5]}\n_ _ _\n{a[6]}|{a[7]}|{a[8]}''');



    
    
    if  (a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;






    print("")
    print(f"User-2..choose {user2_choice}\'s position.....");x+=1;
    print(f'''{a[0]}|{a[1]}|{a[2]}\n_ _ _\n{a[3]}|{a[4]}|{a[5]}\n_ _ _\n{a[6]}|{a[7]}|{a[8]}''');
    var2=int(input())










    a[var2-1]=user2_choice;
    print(f'''{a[0]}|{a[1]}|{a[2]}\n_ _ _\n{a[3]}|{a[4]}|{a[5]}\n_ _ _\n{a[6]}|{a[7]}|{a[8]}''');

    
    if  (a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        break;
    elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        break;
    elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;
    elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        break;








   
if  (a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        
elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[0]==a[1] and a[0]==a[2]  and a[0] == user1_choice   ) :
        print(f"{user1_choice} won the match")
        
elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user1_choice   ):
        print(f"{user1_choice} won the match")
        
elif  (a[0]==a[1] and a[0]==a[2]  and a[0] == user2_choice   ) :
        print(f"{user2_choice} won the match")
        
elif(a[3]==a[4] and a[3]==a[5]  and a[3] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[6]==a[7] and a[6]==a[8]  and a[6] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[0]==a[3] and a[0]==a[6]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[1]==a[4] and a[1]==a[7]  and a[1] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[2]==a[5] and a[2]==a[8]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[0]==a[4] and a[0]==a[8]  and a[0] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
elif(a[2]==a[4] and a[2]==a[6]  and a[2] == user2_choice   ):
        print(f"{user2_choice} won the match")
        
else:
        print("The match is draw")