#read
file = open("demo.txt",mode='r')
read_data = file.read()
print(read_data)
file.close()

#readline
file = open("demo.txt",mode='r')
read_data = file.readline()
print(read_data)
file.close()

#append
file = open("demo.txt",mode='a')
write_data = file.write("Welcome to pythonlife")
file.close()

#write
print ("********write**********")
file = open("demo.txt",mode='w')
write_data = file.write("Welcome to Python Learning")
file.close()

#writeline
emp_data = ["kiran\n","ayesha\n","sudheer\n","basheer"]
file = open("demo123.txt",mode = 'w')
write_data = file.writelines(emp_data)
file.close()

#mode w+
file = open("demo2.txt",mode='w+')
write_data = file.write("Python data")
file.seek(0)
print(file.read())
file.close()

#file rename
import os
fn="demo.txt"
nn="sampledemo.txt"
os.rename(fn,nn)

#file read
file = open("C:\python_project\demo.txt",mode='r')
read_data = file.read()
print(read_data)
file.close()

#mode(a+)
file = open("demo.txt",mode = 'a+')
write_data = file.write("welcome to pythonlife")
print(file.tell())
file.seek()
read_data = file.read()
print(read_data)
file.close()

#mode(r+)
file = open("demo.txt",mode = 'r+')
write_data = file.write("hi everyone")
print(file.tell())
file.seek(0)
read_data = file.read()
print(read_data)
file.close()