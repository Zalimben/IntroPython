
def log(funcion):
    def printLog(fn):
        print('Se llama función:', funcion.__name__)
    return printLog
