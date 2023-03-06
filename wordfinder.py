"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    
    def __init__(self,path):

        """set path to link specified in function """
        self.path = path
        """open file and save to words"""
        words = open(self.path, "r")
        """set words read in file in words prop"""
        self.words = words.read()
        """set all_words prop to list of string where each word is split by whitespaces """
        self.all_words = list(map(str,self.words.split()))
        """close file after reading"""
        words.close()
        print (f"{len(self.words)} words read")

    def __repr__(self):
        """Show self representation"""
        return f"<WordFinder file_path={self.path}"
        
    def random(self):
        """pick a random word in path"""
        return random.choice(self.all_words)

class SpecialWordFinder(WordFinder):
    def __init__(self,path):
        super().__init__(path)
    def random(self):
        self.all_words = [word for word in self.words.split() if word[0]!= "#"]
        return random.choice(self.all_words)


    
    