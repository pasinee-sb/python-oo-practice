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
        self.start = self.next = start

    def __repr__(self):
        """Show self representation"""
        return f"<SerialGenerator start={self.start} next={self.next}"

    def generate(self):
        """Everytime function is called, increase number by one"""
        self.next = self.next+1
        return self.next-1

    def reset(self):
        """Resets the number to starting number"""
        self.next = self.start


        

