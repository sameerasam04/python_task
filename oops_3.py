#Encapsulation
# public
class gfather():
    def __init__ (self,a):
        self.a = a
        print(f"this is base class {a}")
class father(gfather):
    def display (self):
        print(f"this is derived class {self.a}")
obj = father("100cr")
obj.display()

# protect
class gfather():
    def __init__ (self,a):
        self._a = a
        print(f"this is base class {a}")
class father(gfather):
    def display (self):
        print(f"this is derived class {self._a}")
obj = father("100cr")
obj.display()

# private
class gfather():
    def __init__ (self,a):
        self.__a = a
        print(f"this is base class {a}")
class father(gfather):
    def display (self):
        print(f"this is derived class {self.a}")
obj = father("100cr")
obj.display()

# Abstract class 
from abc import ABC , abstractmethod 
class  abstract_demo(ABC):
    @abstractmethod
    def display (self):
        pass
    @abstractmethod
    def display2 (self):
        pass
class demo ("abstaract_demo"):
    def display(self):
        print(f"implementation done in derived class")
    def display2 (self):
        print(f"implementation 2 done")
obj = demo()
obj.display()
obj.display2()

# Abstract method
from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class gpay(payment):
    def pay(self):
        print(f"payment done via gpay")
        
class phonepay(payment):
    def pay(self):
        print(f"payment done via phonepay")
class cred(payment):
    def pay(self):
        print(f"payment done via cred")  
obj = gpay()
obj.pay()
obj = phonepay()
obj.pay()
obj = cred()
obj.pay()
                                         
                                            
