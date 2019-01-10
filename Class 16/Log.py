import datetime
class Log:

    def log(self, msj, severity):
        # the severity (E, W, I) (Error, Warning, Informational)
        line = str(datetime.datetime.now()) + "  " + severity + "  "+"  " + msj
        with open("log.txt", 'a+') as f:
            f.write(line)


