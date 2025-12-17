#Inheritance

print ("**********Inheritance***********")
class feature_phone():
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    def make_call(self,number):
        print(f"calling {number} from {self.brand} {self.model}")
    def send_message(self,message,number):
        print(f"sending {message} from {number}")
#nokia = feature_phone("nokia",2010,"black")   
#nokia.make_call(12345678)
#nokia.send_message("hello everyone",12345678)      

class smartphone(feature_phone):
    def camera(self):
        print(f"photo captured")
    def gaming(self):
        print(f"playing games {self.brand}")   
    def browsing(self,browser):
        print(f"Internet browsing {browser}")  
nokia = smartphone("nokia",2012,"Black") 
nokia.make_call(12345678)
nokia.send_message("Pythonlife",12345678)
nokia.camera()
nokia.gaming()
nokia.browsing("chrome")

print ("********Hierarchical Inheritance**********")
class a():
    def parent(self):
        print("this is parent class")
class b(a):
    def child1(self):
        print(f"This is child 1 class")
class c(a):        
    def child2(self):
        print(f"This is child 2 class")
obj1 = b()
obj1.child1()
obj1.parent()  

obj2 = c()
obj2.child2()
obj2.parent()      

print ("******Multiple  Inheritance*********")
class gfather():
    def output(self):
        print(f"earned 100 Cr properties")
class father(gfather):
    def output1(self):
        print(f"This is father class")
class child(father):
    def output2(self):
        print(f"this is child class")
    def sample(self):
        print(f"started ABC company")
obj=child()
obj.output()
obj.output1()
obj.output2()
obj.sample()                                

print("************Next example***********")

class parent1():
    def father(self):
        print("This is the father class")
class parent2():
    def mother(self):
        print("This is mother class")
class kid(parent1,parent2):
    def child(self):
        print("This is child")
obja=kid()  
obja.father()
obja.mother()
obja.child()  

print("**************Polymorphism***********") 
a=5
b=10
print(a+b)    
c="sameera"
d="sam"
print(c+d)

print("********method overloading*******")
class calculator():
    def sample2(self,a1,b1,c1=None):
        print(a1,b1)
    def sample2(self,a1=None,b1=None,c1=None):
        print(a1,b1,c1)
objc=calculator()
objc.sample2(10,20)
objc.sample2(10,20,30)

print("***********method overriding**********")
class gfather():
    def details(self,a):
        print(f"this is gfather class")
class father(gfather):
    def details(self,a):
        print(f"this is father class")  
objd=father()
objd.details("100cr")              

print("*******ATM project*********")

# ---------- Base Class ----------
class ATM:
    def __init__(self):
        self.balance = 0

    def credit(self, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            self.balance += amount
            print(f"Rs {amount} credited.")

    def debit(self, amount):
            pass

    def show_balance(self):
        print(f"Current Balance: Rs {self.balance}")


# ---------- Old ATM (500 notes) ----------
class OldATM(ATM):
    
    def debit(self, amount):
        if amount <= 0:
            print("Enter positive amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        if amount % 500 != 0:
            print("Old ATM dispenses only Rs 500 notes.")
            return

        notes = amount // 500
        self.balance -= amount

        print(f"Withdrawn Rs {amount}")
        print(f"Dispensed Notes: {notes} x Rs 500")


# ---------- New ATM (200 notes) ----------
class NewATM(ATM):

    def debit(self, amount):
        if amount <= 0:
            print("Enter positive amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        if amount % 200 != 0:
            print("New ATM dispenses only Rs 200 notes.")
            return

        notes = amount // 200
        self.balance -= amount

        print(f"Withdrawn Rs {amount}")
        print(f"Dispensed Notes: {notes} x Rs 200")


# ---------- MAIN PROGRAM ----------
print("Select ATM Type:")
print("1. Old ATM (Rs 500 notes)")
print("2. New ATM (Rs 200 notes)")

atm_choice = input("Enter choice (1 or 2): ")


if atm_choice == "1":
    atm = OldATM()
else:
    atm = NewATM()


while True:
    print("\nATM Menu")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to credit: "))
        atm.credit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to debit: "))
        atm.debit(amt)   

    elif choice == "3":
        atm.show_balance()

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid option!")
