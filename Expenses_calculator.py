name=input("Please enter your name :")
salary=float(input("Please enter your salary :"))

print("Expense Calculator")
Grocery_bill=float(input("Enter your Grocery Bill :"))
KE_bill=float(input("Enter your KE-Bill :"))
Gas_bill=float(input("Enter your Gas Bill :"))
Internet=float(input("Enter your internet Bill :"))
Water_bill=float(input("Enter your Water Bill :"))
Jamadar=float(input("Enter your Jamadar Bill :"))
super_card=float(input("Enter your super_card Bill :"))
Transport=float(input("Enter your Transport Bill :"))
own_house=input("Do you in your own house :")

if own_house.lower() == "no":
    rent=float(input("Enter your rent"))
else:
    rent = 0


married=input("Are you married ?")
if married.lower() =="yes":
    child=int(input("How many children do you have ?"))
    if child > 0:
        child_expenses=float(input("Enter your child expenses :"))
    else:
        child_expenses = 0
Total_Expenses =Grocery_bill+KE_bill+Gas_bill+Internet+Water_bill+Jamadar+super_card+Transport+rent+child_expenses
total_saving=salary-Total_Expenses
if salary > Total_Expenses:
    print(f"{name} \nYour saving are : {total_saving} \n you should take savings plan \nkindly visit your nearest meezan bank")
elif salary == Total_Expenses :
    print("You should take major step to increase your income and contact dholu bholu")
else:
    print("Please decrease your expenses")
print(f"Your Salary is : {salary} \n Your total expenses is : {Total_Expenses} \n Total saving is :{total_saving}")


