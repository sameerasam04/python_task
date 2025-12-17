class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"{self.brand} laptop costs ${self.price}")

# Create objects
l1 = Laptop("dell",13000)
l2 = Laptop("lenovo", 20000)

# Use method
l1.show_details()
l2.show_details()
