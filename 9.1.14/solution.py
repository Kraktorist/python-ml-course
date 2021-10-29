from os import name
import tempfile

class File:
    
    def __init__(self, path):
        with open(path,'a') as f:
            self.path = path 

    def read(self):
        with open(self.path) as f:
            return(''.join(f.readlines()))

    def write(self, text):
        with open(self.path,'w+') as f:
            return f.write(text,)

    def __add__(self, other):
        text1 = str.encode(self.read())
        text2 = str.encode(other.read())
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(text1)
            f.write(text2)
            filename = f.name
        return File(filename)


    def __str__(self):
        return self.path

    def __iter__(self):
        return open(self.path)


