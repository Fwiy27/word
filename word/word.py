class Word:
    def __init__(self, words_file_location: str = 'word/default_words.txt', bonus_letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y']) -> None:
        self.words_file_location = words_file_location
        self.bonus_letters = bonus_letters
        
    def reset_words(self) -> None:
        pass
    
    def reset_letters(self, output = True) -> None:
        self.letters_not_used = self.bonus_letters.copy()
        if output:
            print('Reset Letters Used')
    
    def get_word(self, syllable: str) -> str:
        pass
    
    def get_best_word(self, syllable: str) -> str:
        pass