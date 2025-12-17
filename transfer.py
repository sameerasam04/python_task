#task1
#1.break in a while loop
numbers=[25,30,20,40,15,25]
total=0
for num in numbers:
    total +=num
    if total>100:
       print("sum exceeded 100")
       break
else:
    print("total sum:",total)
#task2
#2.continue in a for loop

for num in range(1,600):
   if num%2==0:
           continue
   print(num)
#task3
#3.use pass in conditionl statements
number=int(input("enter a number: "))
if number%2==0:
   print("Even")
else:
   pass
#task4
#4.combing transfer statement

words=["hello","skip","world","python","break","end"]
for word in words:
    if word=="break":
        break
    elif word=="skip":
        continue
    else:
        print(word)
        