"""
This script is a simple personal/business expense tracker written in Python.

Purpose:
---------
The program helps users manage their business income and track their expenses.
It collects information such as the total income, the source of income, and multiple expense details (amount, date, and description).
It then displays a summary of all expenses and suggests a breakdown of the remaining savings into various categories.

Functionality:
--------------
1. Takes user input for:
   - Total income
   - Source of income
   - Multiple expenses including:
     - Amount
     - Date or day of the expense
     - Description of the expense

2. Stores each set of expense data in separate dictionaries:
   - `total_amount`: for storing expense amounts
   - `total_date`: for storing corresponding dates
   - `total_discription`: for storing descriptions

3. Prints a summary of all expenses in a readable format.

4. Calculates:
   - Total expenses
   - Remaining income (income - total expenses)

5. Suggests how to allocate the remaining income:
   - 50% to bank savings
   - 25% to parents
   - 10% for daily expenses
   - 12% for school donations
   - 3% as a personal bonus

Usage:
------
Run the script in a Python environment.
Follow prompts to enter income and expense details.
The script will output a financial summary and savings recommendation.

Note:
-----
- Make sure to input numeric values for amounts.
- The script assumes correct input from the user; input validation can be added for robustness.
- Expense entries are stored using incremental keys like 'Amount 1', 'Amount 2', etc.
"""









#variables total_amount,total_date and total_discription
total_amount = {} ;
total_date = {} ;
total_discription = {} ;

income = int(input("Enter total income of your business (\'monthly incomeor etc.,\')\n"))
source = input("Enter your source of income\n")
print("Total expence details ")
print("your total income is"+str(income)+ f".which is from {source}\n")

print("Enter your expence details:")
n = 1
adding = "y"
while  adding.lower() == "y": 
        amount = int(input("Enter expence amount\n"))
        date = input("Enter the date or day of that expence\n")
        discription = input("Enter the discription of that expence\n")
        adding = input("Do you want to add 1 more details (Type 'y' for yes or 'n' for no)\n")
        total_amount[f"Amount {n}"]= amount
        total_date[f"date {n}"]= f"{date}"
        total_discription[f"discription {n}"]= f"{discription}"
        n+=1
        if adding.lower() == "y":
            continue;
        else :
            break; 



length_total_amount = len(total_amount)
var1 =list(total_amount.values())
var2 =list(total_date.values())
var3 =list(total_discription.values())
m = 1
for i in  range(length_total_amount):
        print(f"{m}. You spent {var1[i]} rupees for {var3[i]} on {var2[i]}")   
        m+=1


  
total_expence =  sum(var1)
remaining = income - total_expence 
print(f"""
As per above values your income will be {income} rupees and from {source}.
you saved {remaining} rupees,
*you can....*
Put {remaining*(50/100)} rupees in bank ,,because savings is important
Give {remaining*(25/100)} rupees to your parents,, :) It is good idea.
and {remaining*(10/100)} rupees to you ,, use it for your daily expences
and {remaining*(12/100)} rupees donate to schools.
and {remaining*(3/100)} rupees are bonous of your hard work 


""")





#output will look like

"""
Enter total income of your business ('monthly incomeor etc.,')
80000
Enter your source of income
Enginner
Total expence details 
your total income is80000.which is from Enginner

Enter your expence details:
Enter expence amount
80
Enter the date or day of that expence
2/2/24
Enter the discription of that expence
pen
Do you want to add 1 more details (Type 'y' for yes or 'n' for no)
y
Enter expence amount
52
Enter the date or day of that expence
sunday
Enter the discription of that expence
book
Do you want to add 1 more details (Type 'y' for yes or 'n' for no)
y
Enter expence amount
34000
Enter the date or day of that expence
3/4/24
Enter the discription of that expence
current bill
Do you want to add 1 more details (Type 'y' for yes or 'n' for no)
n
1. You spent 80 rupees for pen on 2/2/24
2. You spent 52 rupees for book on sunday
3. You spent 34000 rupees for current bill on 3/4/24

As per above values your income will be 80000 rupees and from Enginner.
you saved 45868 rupees,
*you can....*
Put 22934.0 rupees in bank ,,because savings is important
Give 11467.0 rupees to your parents,, :) It is good idea.
and 4586.8 rupees to you ,, use it for your daily expences
and 5504.16 rupees donate to schools.
and 1376.04 rupees are bonous of your hard work


"""
