#Simple quizz game
marks = 0
print("Write answers for each 5 question")
q1 = input("q1.What does CPU stand for? \n")
if q1.lower() == "Central Processing Unit".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:Central Processing Unit")

q2 = input("q2 .What does RAM stands for? \n")
if q2.lower() == "Random Access Memory".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:Random Access Memory")

q3 = input("q3.What type of device connects your computer to the internet?\n")
if q3.lower() == "Router".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:Router")

q4 = input("q4. What does  'cmd' typically refer to on a Windows PC?\n")
if q4.lower() == "Command Prompt".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A: Command Prompt ")
 
 
q5 = input("q5.What is the part of the computer that displays information and images?\n")
if q5.lower() == "Monitor".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A: Monitor")




""" Corrrect Answers   
    1.What does CPU stand for?
      Central Processing Unit
    2.What does RAM stands for? 
      Random Access Memory
    3.What type of device connects your computer to the internet?
      Router
    4.What does  "cmd" typically refer to on a Windows PC?
      Command Prompt 
    5. What is the part of the computer that displays information and images?
      Monitor
      """




print("Multiple choice questions , Write full answer example, C.Monitor\n\n\n ")
q6 = input("""q6.Which of the following is an INPUT device?

A.Monitor
B.Keyboard 
C.CPU
D.RAM \n""")
if q6.lower() == "B.Keyboard".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A: B.Keyboard  ")


q7 = input("""q7.What is the main function of an operating system?

A.To browse the internet
B.To manage hardware and software resources  
C.To play games
D.To write documents\n""")
if q7.lower() == "B.To manage hardware and software resources".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A: B.To manage hardware and software resources  ")


q8 = input("""q8.In a web address, what does the "http" stand for?

A.Hyper Text Transfer Protocol 
B.High Tech Personalization
C.Home Texting Platform
D.Huge Textual Portal\n""")
if q8.lower() == "A.Hyper Text Transfer Protocol".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A: A.Hyper Text Transfer Protocol ")


q9 = input("""q9.What is the purpose of formatting a hard drive?

A.To increase storage space
B.To erase and prepare data for storage  
C.To improve internet speed
D.To change the color of the computer case\n""")
if q9.lower() == "B.To erase and prepare data for storage".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:  B.To erase and prepare data for storage")




q10 = input("""q10.What is the extension for a compressed file format?

A) .txt
B) .doc
C) .zip  
D) .exe\n""")

if q10.lower() == "C) .zip".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:  C) .zip")




q11 = input("""Bonus MCQ ,What is the term for a set of instructions that tells a computer how to perform a specific task?
* A.Hardware
* B.Software  
* C.Network
* D.User Interface\n""")
if q11.lower() == "B.Software".lower():
    print("correct answer")    
    marks+=1
else:
    print("wrong answer")
    print("A:  B.Software")

print(f"well test is over you got {marks} out of 10\n")
if marks > 10:
    print("Outstanding")
elif marks == 10:
    print("Good")
elif marks >=7 :
    print("not bad")
elif marks >4 :
    print("it's okay")
else:
    print|(" Fail")












