'''Exercise 1 Sum of Squares
 Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a 
for loop.'''

sum=0
for i in range(1,6):
    result=i**2
    sum+=result
print(sum)

'''Write a Python program that uses a 
while loop to print a countdown from 5 to 1.'''

num=5
while num>=1:
    print(num)
    num+=-1

'''Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop'''

table=int(input("enter the table:"))
for i in range(1,11):
        for j in range(1,2):
                print(f"{table}x{i}={table*i}")

'''Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive).'''

sum=0
for i in range(1,11):
        if i%2==0:
                sum+=i
print(sum)

#Calculate the sum of all numbers from 1 to a given number

num=int(input("enter the num:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(f"sum of all numbers from 1 to {num} = {sum}")

'''Exercise 6
 Display numbers from a list using loop'''

list=[1,2,3,4]
for i in list:
    print(i)

'''Exercise 7
Display numbers from -10 to -1 using for loop'''

for i in range(-10,0):
    print(i)

'''Write a Python program to print the cube of all numbers from 1 to a given 
number'''

num=int(input("enter the num:"))
for i in range(1,num+1):
    result=i**3
    print(result)
 
'''Write a Python program to print the cube of all numbers from 1 to a given 
number and sum it'''

num=int(input("enter the num:"))
sum=0
for i in range(1,num+1):
    result=i**3
    sum+=result
print(sum)

