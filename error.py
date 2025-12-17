#types of error
#1.syntax error
#2.logical error
#3.runtime error

#logical errors
num_1 = 10
num_2 = 5
result = num_1 - num_2
print(result)

#syntax error
for i in "pythonlife":
    print(i)

#runtime error (which disturbs the flow of execution)

num_1 = int(input("enter the number1: "))
num_2 = int(input("enter the number2: "))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
try:
    print(num_1 / num_2)
except:
    print("error occured")
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)


#value error
try:
    num_1 = int(input("enter the number1: "))
    num_2 = int(input("enter the number2: "))
except ValueError as e:
    print(e)
else:
    print(num_1+num_2)

#zero division error
num_1 = int(input("enter the number1: "))
num_2 = int(input("enter the number2: "))
try:
    print(num_1/num_2)
except ZeroDivisionError as e:
    print(e)


#index error
sample = [20,23,49,12]
try:
    print(sample[9])
except IndexError as e:
    print(e)

#type error
a=8
b='10' 
try:
    print(a+b)
except TypeError as e:
    print(e)

#filenotfounderror
try:
    file=open("python.txt,","r")
except FileNotFoundError as e:
    print(e)

#keyerror
my_dict= {'name': 'Laptop',1: 'Dell', 'price': 1200}
try:
    print(my_dict["city"])
except KeyError as e :
    print(e)


#attribute error
class student:
    def __init__(self,name):
        self.name=name
s=student("sameera")
try:
    print(s.age)
except AttributeError as e:
    print(e)

#overflowerror
import math
try:
    print(math.exp(1000))
except OverflowError as e:
    print(e)


#exception
num_1 = int(input("enter the number1: "))
num_2 = int(input("enter the number2: "))
try:
    print(num_1/num_2)
except Exception as e:
    print(e)



