"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
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
        self.open = open(self.path, "r")
        """set words read in file in words prop"""
        self.words = self.open.read()
        """set all_words prop to list of string where each word is split by whitespaces """
        self.all_words = list(map(str,self.words.split()))
        
        print (f"{len(self.words)} words read")

    def __repr__(self):
        """Show self representation"""
        return f"<WordFinder file_path={self.path}"
        
    def random(self):
        """pick a random word in path"""
        return random.choice(self.all_words)

class SpecialWordFinder(WordFinder):

    """
    >>> wf = SpecialWordFinder("special_word_test.txt")
    >>> random.seed(2)
    >>> wf.random()
    
    

    """
    def __init__(self,path):
        super().__init__(path)
        split_it = list(map(str,self.words.splitlines()))
        self.all_words = [word for word in split_it if not word.startswith("#") and word != "" ]
    
    