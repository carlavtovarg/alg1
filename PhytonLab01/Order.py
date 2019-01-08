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
                total_gst += float(x.calculate_gst())
        return total_gst

    def get_total_qst(self):
        total_qst = 0
        for x in self.items:
            if x.is_taxable():
                total_qst += float(x.calculate_qst())
        return total_qst

    def total_price(self):
        total_price = 0
        for x in self.items:
            total_price += float(x.get_price())
        return total_price

    def print_items(self):
        for x in self.items:
            x.print_item(50)

    def generate_receipt(self):
        print("Order Number: {0}".format(self.sku))
        print("Order Date : {0}".format(self.date_print))
        self.print_items()
        print("Sub Total: {0}".format(self.total_price()))
        print("Total GST : {0}".format(self.get_total_gst()))
        print("Total QST : {0}".format(self.get_total_qst()))


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

New_Order.generate_receipt()

