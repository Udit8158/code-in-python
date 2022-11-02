import csv


# Making an Item class


class Item:
    discount_percent_rate = 0.8  # when use 20 percent discount
    all_items = []

    # constractor function  -> create new instances and must have a parameter which point to the every instance
    def __init__(self, name: str, price: float, quantity=0):
        # Validating receiving parameters
        assert price >= 0, f"Price {price} should be greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to zero"

        # Assigning variables
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append the instances in the all_items list
        Item.all_items.append(self)

    # Method
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount_percent_rate

    # Magic method to beautify the instances elements on the all list
    def __repr__(self):
        return f"name = {self.name}, price = {self.price}, quantity = {self.quantity}"

    # Now Making Instances (objects) from csv file via this class method
    #   -> Accessible only from class level , and must have a parameter which is class itself
    @classmethod
    def instance_initiation(cls):
        # Opening csv file
        with open("items.csv", mode='r') as file:
            # read csv file as a list of dict
            csv_file = csv.DictReader(file)
            items = list(csv_file)

            for item in items:
                cls(item["name"], float(item["price"]), int(item["quantity"]))

    # Static Method -> It is a regular function
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False