from Item import Item
import datetime


class Order:
    """this is the class for the order"""
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
        self.gran_total = 0

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

    def grand_total(self):
        self.gran_total = float(self.total_price()) + float(self.get_total_qst()) + float(self.get_total_gst())
        return self.gran_total

    def generate_receipt(self):

        print("\n")
        print("Order Number: {0}".format(self.sku).center(50))
        print("Order Date : {0}".format(self.date_print).center(50))
        print("\n")
        self.print_items()
        print("\n")
        print("Sub Total: ${:0,.2f}".format(self.total_price()).center(50))
        print("Total GST : ${:0,.2f}".format(self.get_total_gst()).center(50))
        print("Total QST : ${:0,.2f}".format(self.get_total_qst()).center(50))
        print("Grand Total: ${:0,.2f}".format(self.grand_total()).center(50))


New_Order = Order()
cont = "y"

while cont != "n" and cont != "N":
    item_sku = input("What is the sku of the item to add? >>")
    item_name = input("What is the name of the item to add? >>")
    item_cost = input("How much does the item cost? >>")
    item_tax_p = input("Is the item taxable? (Y/N) >>")
    cont = input("Add another item? (Y/N) >>")
    if item_tax_p == "y":
        item_tax = True
    else:
        item_tax = False
    try:
        item_cost = float(item_cost)
        item_cost = "{:0,.2f}".format(item_cost)
        new_item = Item(item_sku, item_name, item_cost, item_tax)
        New_Order.add_item(new_item)
        create_receipt = True
    except:
        print("The last item could not be create, please try again")
        create_receipt = False
        cont = "y"
if create_receipt != False:
    New_Order.generate_receipt()

