# A shop management program
from item import Item
from phone import Phone

# creating instances from class

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# Item.instance_initiation()
# print(Item.all_items)
# print(Item.is_integer(3.0))  # True

# -------- INHERITANCE --------------


phone1 = Phone("iPhone", 100, 23, 2)
print(phone1.broken_phones)  # 2
print(phone1.calculate_good_phones())  # 21
phone1.apply_discount()
print(phone1.price)

print(Item.all_items)
print(Phone.all_items)
