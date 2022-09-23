import csv


class Item:
    def __init__(self, name: str, price: float, quantity=0):

        self.__name = name
        self.price = price
        self.quantity = quantity

    ## Proper Decorator = Read-Only Attribute
    @property
    def name(self):        
        return self.__name

    @name.setter
    def name(self, newName):
        if len(newName)>10:
            raise Exception("Name is too long")
        else:
            self.__name = newName

item1 = Item("Phone",100,5)
# print(item1.name)
item1.name = "New Phone"
print(item1.name)





# item1.name = "new Phone"
# print(item1.name)













'''
    #############################################################################
    ## poperty decorator turns a function into a attribute (read only)
    ## Proper Decorator = Read-Only Attribute
    # @property
    # def another_name(self):
    #     return "name property"
    #############################################################################

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

'''


#############################################################################
# item1.another_name = "BBB"
# print(item1.another_name)
#############################################################################