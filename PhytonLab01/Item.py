class Item:
    qst_tax = 0
    gst_tax = 0
    #constructor

    def __init__(self, sku, name, price, taxable=False):
        self.sku = sku
        self.name = name
        self.__price = price
        self.__taxable = taxable

    def is_taxable(self):
        return self.__taxable

    def get_price(self):
        return self.__price

    def calculate_qst(self):
        self.qst_tax = self.__price * 9.975 / 100
        return self.qst_tax

    def calculate_gst(self):
        self.gst_tax = self.__price * 5 / 100
        return self.gst_tax

    def print_item(self, len_line):
        part_line = self.name  + "$" + str(self.__price)
        len_part_line = int(len_line) - len(part_line)
        string_points = "." * int(len_part_line)
        line = self.name + string_points + "$" + str(self.__price)
        if self.__taxable:
            line = line + "T"
        return line

# Some test from the code:
item1= Item(25, "pasta", 100, True)
item2= Item(50, "cafe", 100)
print(item1.name)
print(item1.is_taxable())
print(item2.calculate_qst())
print(item2.calculate_gst())
print(item1.print_item(50))

print(item2.print_item(50))



