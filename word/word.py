from word.utils import get_random_available_word, get_best_word
import os

class Word:
    def __init__(self, words_file_location: str = os.path.join(os.path.dirname(__file__), 'default_words.txt'), bonus_letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y']) -> None:
        self.words_file_location = words_file_location
        self.bonus_letters = bonus_letters
        
        self.reset_letters(output = False)
        self.reset_words(output = False)
        
    def reset_words(self, output = True) -> None:
        with open(self.words_file_location) as file:
            self.words = file.read().split()
        if output:
            print('Reset Words Used')
    
    def reset_letters(self, output = True) -> None:
        self.letters_not_used = self.bonus_letters.copy()
        if output:
            print('Reset Letters Used')
    
    def get_word(self, syllable: str) -> str:
        return get_random_available_word(syllable, self.words)
    
    def get_best_word(self, syllable: str) -> str:
        return get_best_word(syllable, self.words, self.letters_not_used)
    
    def choose_word(self, word: str) -> None:
        self.words.remove(word)
        for letter in word:
            if letter.lower() in self.letters_not_used:
                self.letters_not_used.remove(letter.lower())
                
        if len(self.letters_not_used) == 0:
            self.reset_letters()