class Taxes:
    """This class set and get the taxes values"""
    def __init__(self):
        """Those are the percent taxes divided by 100"""
        self.__qst_percent_tax = 0.09975
        self.__gst_percent_tax = 0.05

    def set_qst_percent_taxes(self,qst_percent_tax):
        self.__qst_percent_tax = float(qst_percent_tax)/100

    def get_qst_percent_taxes(self):
        return self.__qst_percent_tax

    def set_gst_percent_taxes(self, gst_percent_tax):
        self.__gst_percent_tax = float(gst_percent_tax)/100

    def get_gst_percent_taxes(self):
        return self.__gst_percent_tax

