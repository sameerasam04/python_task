#task1
#Vowel Checker:
char_=input("enter the char:")
vowels="aeiouAEIOU"
if vowels in char_:
    print(f"char is in {vowels},so it is a vowel")
else:
    print(f"char is not in {vowels},so it is not a vowel")

#task2
#age group classification
age=int(input("enter the age:"))
if age <0:
    print("not a valid info")
elif 0<=age<=12:
    print("he/she is a child")
elif 13<=age<=17:
    print("he/she is a teenager")
elif 18<=age<=64:
    print("he/she is a adult")
else:
    print("he/she is a senior")


#task3
#Number Classifier:
int_value=int(input("enter the integer value:"))
if int_value >0:
    print("it is positive")
elif int_value <0:
    print("it is nagative")
else:
    print("it is zero")


#task4
#Leap Year Checker:
year_val=int(input("enter the year:"))
if year_val%400==0 or year_val%4==0 and year_val%100!=0:
    print(f"{year_val} is a leapyear")
else:
    print(f"{year_val} is not a leapyear")

#task5
#Calculator:
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
operator=input("enter the operator:")
if operator=="+":
    print(f"{num1}+{num2} is {num1+num2} ")
else:
    print(f"please take + operator")


#task6
#Short Hand If:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
  


#task7
#discount calculator
original_price=int(input("enter the originalprice:"))
discount_percentage=int(input("enter discount percentage:"))
discount=original_price*discount_percentage/100
original_price=original_price-discount
print(original_price)


#task8
#bmi calculator
weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
bmi_calculation=weight/height**2
print(bmi_calculation)








