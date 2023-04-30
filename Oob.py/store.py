class Item:
    pay_rate = 0.8 #Pay rate after discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to received arguments
        assert price >=0, f'Price {price} should not be less than zero'
        assert quantity >=0, f'Quantity {quantity} should not be less than zero'

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    

'''
item1 = Item('phone', 100, 3)
item1.apply_discount()
print(item1.calculate_total_price())
#print(item1.__dict__) #prints the attributes for the instance level
#print(Item.__dict__) #prints the attributes for the class level


item2 = Item('laptop', 1000, 2)
item2.pay_rate = 0.9
item2.apply_discount()
print(item2.calculate_total_price())
'''

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)


print(Item.all)