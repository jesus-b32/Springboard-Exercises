from random import choice
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read
    """

    def __init__(self, file_path):
        # self.file_path = file_path
        self.word_list = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                self.word_list.append(line)

        print(f'{len(self.word_list)} words read')
        

    def random(self):
        return choice(self.word_list)
    

class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)

    def random(self):
        line =  super().random()

        while True:
            if not (line[0] == '#' or line.isspace()):
                return line
