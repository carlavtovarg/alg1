from Item import Item
import datetime
import decimal


class Order:
    last_sku_used = 0

    def __init__(self):
        self.sku = Order.last_sku_used + 1
        self.items = []
        date_to_print = ""
        x = datetime.datetime.now()
        date_to_print += x.strftime("%Y-%m-%d %I:%M")
        date_to_print += x.strftime("%p").lower()
        self.date_print = date_to_print
        Order.last_sku_used = self.sku

    def add_item(self, item: Item):
        self.items.append(item)

    def get_item_count(self):
        return len(self.items)

    def get_total_gst(self):
        total_gst = 0
        for x in self.items:
            if x.is_taxable():
                total_gst += decimal.Decimal(x.calculate_gst())

    def get_total_qst(self):
        total_qst = 0
        for x in self.items:
            if x.is_taxable():
                total_qst += decimal.Decimal(x.calculate_qst())

    def total_price(self):
        total_price = 0
        for x in self.items:
            print(x.get_price())
            total_price += decimal.Decimal(x.get_price())
        return total_price

    def print_items(self):
        for x in self.items:
            x.print_item(50)

    def generate_receipt(self):

New_Order = Order()
cont = "y"

while cont != "n":
    item_sku = input("What is the sku of the item to add? >>")
    item_name = input("What is the name of the item to add? >>")
    item_cost = input("How much does the item cost? >>")
    item_tax_promp = input("Is the item taxable? (Y/N) >>")
    if item_tax_promp == "y":
        item_tax = True
    else:
        item_tax = False
    cont = input("Add another item? (y/n) >>")
    new_item = Item(item_sku, item_name, item_cost, item_tax)
    New_Order.add_item(new_item)

print("Order Number: {0}".format(New_Order.sku))
print("Order Date : {0}".format(New_Order.date_print))
print("Total Price: {0}".format(New_Order.total_price()))

# Some test from the code:
#item1= Item(25, "pasta", 100, True)
#item2= Item(50, "cafe", 100)
#print(item1.name)
#print(item1.is_taxable())
#print(item2.calculate_qst())
#print(item2.print_item(50))
