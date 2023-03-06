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
        """Defines starting number"""
        self.start = start-1

    def generate(self):
        """Everytime function is called, increase number by one"""
        self.start = self.start+1
        return self.start

    def reset(self):
        """Resets the number to starting number"""
        self.start = 99


        

