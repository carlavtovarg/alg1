import datetime

x = datetime.datetime.now()
print (x.strftime("%A"))
print(x.date())
date_to_print = ""
date_to_print += x.strftime("%Y-%m-%d %I:%M")
date_to_print += x.strftime("%p").lower()
print(date_to_print)