"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """FIND WORDS IN A FILE"""
    
    def __init__(self,path):
        """DIRECT TO PATH. OPEN AND READ WORDS IN THE PATH"""
        self.path = path
        words = open(self.path, "r")
        read_words = words.read()
        words.close()
        print (f"{len(read_words)} words read")
        
        
    def read(self):
        """READ WORDS AND RETURN ALL THE WORDS READ"""
        words = open(self.path, "r")
        read_words = words.read()
        all_words = list(map(str,read_words.split()))
        return all_words
        words.close()
        
    
    def random(self):
        """pick a random word in path"""
        return random.choice(self.read())

    
    