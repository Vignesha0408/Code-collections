f = open("mytext.txt","r")
c=[]
for i in f:
    print(i)      #it prints whatever written in file
    c.append(i.split(' '))
print(c)
#c is the list of words



d=0
for v in range(len(c[0])):
   d=d+1
print(d)