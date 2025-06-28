class InvalidOperationError(Exception):
    pass

class stream:
    def __init__(self):
        self.opened = False

    def open(self):
       if self.opened :
           raise IndentationError ("Stream is already opened")
       
    def close(self):
       if not self.opened :
           raise IndentationError ("Stream is already closed")

class NewtworkFileStream(stream):
    def read(self):
        print("Reading data from network")


