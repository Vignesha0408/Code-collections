import random

def generate_password(length):
  num = input("do you required numbers in it (type yes or no)")
  alpha = input("do you required english letters in it (type yes or no)")
  specl = input("do you required some special characters in it (type yes or no)")

  numbers = [1,2,3,4,5,6,7,8,9,0]
  letters_small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  letters_big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  some_spl_characters =["5","@","#","$","%","^","&","*","(",")","#","+","-","+","/","*"]
  print("password generated successfully \n")
  print("password=")
  if num =="yes" and alpha == "no"  and  specl== "no":
    for i in range(1,length+1):
      print(random.choice(numbers),end="")
  elif num =="yes" and alpha == "no"  and  specl== "yes":
    for i in range(1,length+1):
      print(random.choice(numbers+some_spl_characters),end="")
  elif num =="yes" and alpha == "yes"  and  specl== "no":
    for i in range(1,length+1):    
      print(random.choice(numbers+letters_small+letters_big),end="")
  elif num =="yes" and alpha == "yes"  and  specl== "yes":
    for i in range(1,length+1):   
      print(random.choice(numbers+letters_small+letters_big+some_spl_characters),end="")
  elif num =="no" and alpha == "yes"  and  specl== "yes":
    for i in range(1,length+1):   
      print(random.choice( letters_small+letters_big+some_spl_characters),end="")
  elif num =="no" and alpha == "yes"  and  specl== "no":
    for i in range(1,length+1):
      print(random.choice(letters_small+letters_big ),end="")
  elif num =="no" and alpha == "no"  and  specl== "yes":
    for i in range(1,length+1):
      print(random.choice(some_spl_characters),end="")
  elif num =="no" and alpha == "no"  and  specl== "no":
    print("Invalid input from user")
size=int(input("Enter the size of password \n"))
generate_password(size)





