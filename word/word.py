from word.utils import get_random_available_word, get_best_word, get_longest_word
import os

class Word:
    def __init__(self, words_file_location: str = os.path.join(os.path.dirname(__file__), 'default_words.txt'), bonus_letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y']) -> None:
        """Initialize word object

        Args:
            words_file_location (str, optional): Location of words file to read from. Defaults to os.path.join(os.path.dirname(__file__), 'default_words.txt').
            bonus_letters (list[str], optional): List of bonus letters. Defaults to ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y'].
        """
        self._words_file_location = words_file_location
        self._bonus_letters = bonus_letters
        
        self.reset_words(False)
        self.reset_letters(False)
    
    def reset_words(self, output = True) -> None:
        """Reset words used

        Args:
            output (bool, optional): Prints to stdout that words have been reset. Defaults to True.
        """
        self.words: set = set([word.lower() for word in open(self._words_file_location).read().split()])
        print('Reset Word') if output else None
    
    def reset_letters(self, output = True) -> None:
        """Reset letters used

        Args:
            output (bool, optional): Prints to stdout that letters have been reset. Defaults to True.
        """
        self.letters_not_used = self._bonus_letters.copy()
        print('Reset Letters') if output else None
    
    def get_random_word(self, syllable: str, max_length = 0, min_length = 0) -> str:
        """Returns random word with optional length

        Args:
            syllable (str): Syllable to search for
            max_length (int, optional): Maximum word length. Defaults to 0.
            min_length (int, optional): Minimum word length. Defaults to 0.

        Returns:
            str: Random word
        """
        return get_random_available_word(syllable, self.words, max_length, min_length)
    
    def get_best_word(self, syllable: str, max_length = 0, min_length = 0) -> str:
        """Get best word based on letters not used

        Args:
            syllable (str): Syllable to search for
            max_length (int, optional): Maximum word length. Defaults to 0.
            min_length (int, optional): Minimum word length. Defaults to 0.

        Returns:
            str: Best word based on letters not used
        """
        return get_best_word(syllable, self.words, self.letters_not_used, max_length, min_length)
    
    def get_longest_word(self, syllable: str) -> str:
        """Get longest word

        Args:
            syllable (str): Syllable to search for

        Returns:
            str: Longest word
        """
        return get_longest_word(syllable, self.words)
    
    def choose_word(self, word: str) -> None:
        """Removes word from words list and updates letters used

        Args:
            word (str): Word to choose
        """
        self.words.remove(word)
        for letter in word:
            if letter.lower() in self.letters_not_used:
                self.letters_not_used.remove(letter.lower())
        if len(self.letters_not_used) == 0:
            self.reset_letters()
        