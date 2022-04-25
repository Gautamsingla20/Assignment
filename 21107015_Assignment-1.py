# ANSWER 1
# taking input from user of three numbers
import code

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
# finding average of three numbers
avg = (num1 + num2 + num3) / 3
# printing the average
print('Average of given three numbers is :', avg)

# ANSWER 2
Gross_Income = int(input("Enter your income :",))
Dependent = int(input("Enter number of dependent :",))
Standard_deduction = 10000
Dependent_deduction_amount = Dependent * 3000
# printing the value of deduction amount
print("The value of deduction amount is", Dependent_deduction_amount)
Taxable_income = Gross_Income - Standard_deduction - Dependent_deduction_amount
Tax = (20/100) * (Taxable_income)
# printing the value of tax
print("The value of Tax is", Tax)
# printing the value of tax income
print("The value of taxable income is ", Taxable_income)

# ANSWER 3
totaltime = int(input("enter the no. of seconds : "))
if totaltime < 0:
    print(" invalid output")
else:
    (code)
mins = totaltime // 60
secs = totaltime % 60
# printing total time
print(totaltime, "converted to =", mins, "minutes and", secs, "seconds")


# ANSWER 4
n1 = 25
n2 = '25'
n3 = 25.0
# finding sum of n1 , n2 and n3
sum = n1 + int(n2) + int(n3)
ans = str(sum)
# printing ans with its type
print(type(ans), '\n', ans)


# ANSWER 5
from math import *
i = 0
while i <= 345:
    # printing i
    print(i, "---", "sin->", round(sin(radians(i)), 4),",", "cos->", round(cos(radians(i)),4))
    i = i + 15
