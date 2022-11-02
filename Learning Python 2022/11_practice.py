# class Item:
#     discount_rate = 0.8
#
#     def __init__(self, name: str, price: float, quantity=0):
#
#         # Validation
#         assert price >= 0, f"Price {price} should be greater than or equal to 0"
#         assert quantity >= 0, f"Price {quantity} should be greater than or equal to 0"
#
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def calculate_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.discount_rate
#
#
# item1 = Item("iPhone", 100, 20)
# item2 = Item("iPad", 200, 10)
#
# item1.apply_discount()
# print(item1.price)
#
# item2.discount_rate = .5
# item2.apply_discount()
# print(item2.price)
#
#
#
#
