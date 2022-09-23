import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Lec_6.csv','r') as myfile:
            reader = csv.DictReader(myfile)
            items = list(reader)
        for item in items:
            Item(item["name"],float(item["price"]),int(item["quantity"]))
            # print(item)

    @staticmethod
    def is_integer(val):
        if isinstance(val,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        



# Item.instantiate_from_csv()

# print(Item.is_integer(25))

item1 = Item('Phone', 100.0, 1)
print(item1.is_integer(25))
print(Item.all)




# item1.instantiate_from_csv()
# print(Item.all)