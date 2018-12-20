class Item:
    last_sku_used = 0
    def __init__(self, name, price, taxable):
        """here with the sku we use the static variable because each time we intantiate the Item, the sku increase."""
        self.sku = Item.last_sku_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable
        """Here we asigne the last value of self.sku to the last_sku_use, so its no more 0 when create a new object"""
        Item.last_sku_used = self.sku
    @staticmethod
    def print_last_serial_used():
        print(Item.last_sku_used)

a1 = Item("Fist Item", 2.00, True)
a2 = Item("Second Item", 3.00, False)
a3 = Item("Third Item", 3.00, False)
print(a1.sku)
print(a2.sku)
print(a3.sku)
Item.print_last_serial_used()