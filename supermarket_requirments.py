#supermarket bill
name = input("enter your name")

# List of items
lists = '''
Rice        Rs 20/kg
atta        Rs 10/kg
oil         Rs 49/liter
salt        Rs  14/kg
Paneer      Rs  40/kg
soaps       Rs  10/pack
glucose     Rs  140/bottle
'''

#list
price = 0
pricelist = []
totalprice = 0
finalprice = 0
itmlist = []
qualist = []
prilist = []

# Rate for each item
items = {'rice': 20, 'atta': 10, 'oil':49, 'salt':14, 'paneer':40, 'soap':10, 'glucose':140}

while True:
    option = input("press 1 for list or 2 to exit:")
    if option == '2':
        print("thank you for shopping")
        break
    elif option == '1':
         print(lists)

    while True:
        inp1 = input("To buy press 1 or press 2 to exit: ")
        if inp1 == '2':
            print("thank you for shopping")
            break
        elif inp1 == '1':
            item = input("choose your items:").lower()
            while True:
                quantity_input = input("enter quantity:")
                if quantity_input.isdigit():
                    quantity = int(quantity_input)
                    break
                else:
                    print("please enter a valid quantity:")
            if item in items:
                price = quantity * items[item]
                pricelist.append((item, quantity, items[item],price))
                totalprice += price
                itmlist.append(item)
                qualist.append(quantity)
                prilist.append(price)
            else:
                print("selected item is not available. sorry for the inconvenience.")
        if totalprice > 0:
            tax = (totalprice * 12)/100
            finalamount = tax + totalprice

            print(25 * "=", "pythonlife supermarket", 25 * "=")
            print(28 * " ", "banglore")
            print("name:", name, 30 * " ")
            now=datetime.now()
            print(now)
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i,13 * " ", itmlist[i], 8 * " ", qualist[i], 8 * " ", prilist[i])
            print(75 * "-")
            print(50 * " ", 'total amount:', 'rs', totalprice)
            print("tax amount", 50 * " ", 'rs', tax) 
            print(75 * "-")
            print(50 * " ", 'final amount:', 'rs', finalamount)
            print(75 * "-")
            print(20 * " ", "thank you visit again")
            print(75 * "-")

