"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "initialize number generator with a start number"
        self.start = start - 1
        self.counter = 0

    def generate(self):
        "return the next sequential number"
        self.counter += 1
        return self.start + self.counter
    
    def reset(self):
        "return the next sequential number"
        self.counter = 0



