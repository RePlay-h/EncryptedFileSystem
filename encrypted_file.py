from abc import ABC
from abc import abstractmethod

class EFile(ABC):

    def __init__(self):
        supper().__init__() 
    
    @abstractmethod
    def read(filename, flag):

        enc = "utf-32" if flag else "utf-8"

        with open(filename, mode="r",  encoding=enc) as f:
            buf = list(f.read())
            return buf

    @abstractmethod
    def writeBufferTo(buf, filename):
        with open(filename, mode="w+", encoding="utf-32") as f:
            f.write("".join(buf))

    @abstractmethod
    def encode(buffer, delta):

        # use Caesar's cipher for symbols
        for i in range(len(buffer)):
            buffer[i] = chr(ord(buffer[i]) + delta)
        return buffer

    @abstractmethod
    def decode(buffer, delta):

        # use reverse Caesar's cipher for symbols
        for i in range(len(buffer)):
            buffer[i] = chr(ord(buffer[i]) - delta)
        return buffer


