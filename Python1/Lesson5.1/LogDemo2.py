from datetime import datetime
class logger:
    def __init__(self, filename:str):
        self.filename = filename

    def info(self, msg:str):
        with open(self.filename, 'a+') as file:
            file.write(f"{str(datetime.now())} | INFO: {msg}\n")

    def warning(self, msg : str):
        with open(self.filename, 'a+') as file:
            file.write(f"{str(datetime.now())} | WARNING: {msg}\n")

log = logger(filename="logfile.txt")
log.info("成功登录")