
print("1.Temperature.");
def Temp():
    print("Enter the value first,, after select unit")
    value = input()
    print(f"{value}_____:1.Celcius,2.Kelvin,3.Fahrenheit")
    var1=input()
    if var1=="1":
        print("{} Celcius = Enter... 2.Kelvin,3.Fahrenheit ".format(value))
        i=input()
        if i=="2":
            answer=273.15+int(value) 
            print("{} Celcius = {} Kelvin ".format(value,answer))
        if i == "3":
            answer=int(value)*(9/5)+32
            print("{} Celcius = {} Fahrenheit ".format(value,answer))          


    if var1=="2":
        print("{} Kelvin = 1.Celcius,3.Fahrenheit ".format(value))
        i=input()
        if i=="1":
            answer= int(value)-273.15 
            print("{} Kelvin = {} Celcius ".format(value,answer))
        if i == "3":
            answer=(int(value)-273.15)*(9/5)+32
            print("{} Kelvin = {} Fahrenheit ".format(value,answer))  


    if var1=="3": 
        print("{} Fahrenheit = 1.Celcius,2.Kelvin ".format(value))
        i=input()
        if i=="1":
            answer=(int(value) -32)*(5-9)
            print("{} Fahrenheit = {} Celcius ".format(value,answer))
        if i == "2":
            answer=(int(value)-32)*(5/9)+273.15
            print("{} Fahrenheit = {} Kelvin ".format(value,answer))       

Temp()




    
