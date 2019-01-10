from taxes import Taxes


class Item(Taxes):

    def __init__(self, sku: int, name: str, price: float, taxable: bool):
        self.sku = sku
        self.name = name
        self.__price = price
        self.__taxable = taxable
        self.qst_tax = 0
        self.gst_tax = 0
        super().__init__()

    def is_taxable(self):
        return self.__taxable

    def get_price(self):
        return self.__price

    def calculate_qst(self):
        self.qst_tax = float(self.__price) * float(self.get_qst_percent_taxes())
        return self.qst_tax

    def calculate_gst(self):
        self.gst_tax = float(self.__price) * float(self.get_gst_percent_taxes())
        return self.gst_tax

    def print_item(self, len_line):
        part_line = self.name + "$" + str(self.__price)
        len_part_line = int(len_line) - len(part_line)
        string_points = "." * int(len_part_line)
        line = self.name + string_points + "$" + str(self.__price)
        if self.__taxable:
            line = line + "T"
        print(line)





