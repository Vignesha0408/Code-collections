import math
import matplotlib.pyplot as plt
import numpy as np
#Trignametry graphs
print("1.Sine\n2.Cos\n3.Tan\n4.Cosec\n5.Sec\n6.Cot\n7.Log\n8.Exponential\n")
var1=int(input("Enter the choice..."))

if(var1 == 1):
    x = np.linspace(-2*math.pi,2*math.pi,1000)
    y=np.sin(x)
    plt.title("Sin Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 2):
    x = np.linspace(-2*math.pi,2*math.pi,1000)
    y=np.cos(x)
    plt.title("Cos Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 3):
    x = np.linspace(-2*math.pi, 2*math.pi, 1000)
    y=np.tan(x)
    plt.xlim(-3.5*math.pi, 3.5*math.pi) 
    plt.ylim(-7, 7)
    plt.title("Tan Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 4):
    x = np.linspace(-2.5*math.pi, 2.5*math.pi,1000)
    y= 1 /np.sin(x)
    plt.xlim(-3.5*math.pi, 3.5*math.pi)
    plt.ylim(-20, 20)
    plt.title("Cosec Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 5):
    x = np.linspace(-2.5*math.pi, 2.5*math.pi,1000)
    y=1/np.cos(x)
    plt.title("Sec Graph");
    plt.xlim(-3.5*math.pi, 3.5*math.pi)
    plt.ylim(-15, 15)
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 6):  
    x = np.linspace(-2*math.pi, 2*math.pi, 1000)
    y=1/np.tan(x)
    plt.xlim(-3.5*math.pi, 3.5*math.pi) 
    plt.ylim(-10, 10)
    plt.title("Cot Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 7):
    x = np.linspace(0.1, 10, 1000)  
    y = np.log(x)
    plt.title("Log Graph");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()


elif(var1 == 8):
    base = 2
    x = np.linspace(-5, 5, 1000)  
    y = base**x
    plt.title("Exponential");
    plt.xlabel("X axis");
    plt.ylabel("Y axis");
    plt.plot(x, y)
    plt.grid()
    plt.legend()
    plt.show()





else:
    print("Enter valid choice....");
