import os

from Log import Log
import time
msj = "Program started.\n"
new_log = Log()
new_log.log(msj, "I")
time.sleep(5)
msj = "Program finished.\n"
new_log.log(msj, "I")
