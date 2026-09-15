#Hotsl manu small project 
manu = { "Pizza" : 80,
        "Pasta" : 60,
        "Burger" : 50,
        "Coffe" : 50,
        "Fries" : 50,
        "Fried Chicken" : 120,
}

print("==Wellcome To Apna Resturent==")
print(" Pizza = 80Rs\n Pasta = 60Rs\n Burger = 50Rs\n Coffe = 50Rs\n Fries = 50Rs\n Fried Chicken = 120")

order_item = 0

item_1 = input("Enter Your Order = ")
if item_1 in manu:
    order_item += manu[item_1]
    print(f"your {item_1} is added Successfully")
else:
    print(f"Your {item_1} is no avalilable")

another_other = input("Do you want to add more item? (yes/no) = ")
if another_other == "yes":
    item_2 = input("Enter Your Second Order = ")
    if item_2 in manu:
        order_item += manu[item_2]
        print(f"your {item_2} is added Successfully")
    else:
        print(f"item {item_2} is no avalilable")

print(f"your total amount of item to pay = {order_item}")
    

