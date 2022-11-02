from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken_phone=0):
        super().__init__(name, price, quantity)
        assert broken_phone >= 0, f"Number of broken phone should be greater than or equal to 0"

        self.broken_phones = broken_phone

    def calculate_good_phones(self):
        return self.quantity - self.broken_phones
