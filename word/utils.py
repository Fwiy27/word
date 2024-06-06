import random

def substring_in_string(substring: str, full_string: str) -> bool:
    """Check if substring in string ignore capitalization

    Args:
        substring (str): Subtring to look for
        full_string (str): String to look through

    Returns:
        bool: True if substring in string
    """
    return substring.lower() in full_string.lower()

def string_in_list(search_string: str, search_list: list) -> bool:
    return True if search_string.lower() in [word.lower() for word in search_list] else False

def get_all_available_words(syllable: str, word_list: list[str], min_length: int = -1, max_length: int = -1) -> list[str]:
    """Get all words that have syllable in them

    Args:
        syllable (str): Syllable to search for
        word_list (list[str]): Words to search through
        min_length (int, optional): Minimum word length. Defaults to -1.
        max_length (int, optional): Maximum word length. Defaults to -1.

    Returns:
        list[str]: List of all words that have syllable in them
    """
    check_length: bool = False if min_length == -1 and max_length == -1 else True
    
    available: list[str] = []
    
    for word in word_list:
        if substring_in_string(syllable, word):
            if not check_length or min_length <= len(word) <= max_length:
                available.append(word)
    
    return available
                
def get_random_available_word(syllable: str, word_list: list[str], min_length: int = -1, max_length: int = -1) -> str:
    """Get random word that has syllable in it

    Args:
        syllable (str): Syllable to search for
        word_list (list[str]): Words to search through
        min_length (int, optional): Minimum word length. Defaults to -1.
        max_length (int, optional): Maximum word length. Defaults to -1.

    Returns:
        str: Random word with syllable in it
    """
    available: list[str] = get_all_available_words(syllable, word_list, min_length, max_length)
    return random.choice(available)

def weigh_word(available_words: list[str], letters_not_used: list[str]) -> dict[str, int]:
    weighted_words: dict[str, int] = {}
    for word in available_words:
        checked_letters: list[str] = []
        weighted_words[word] = 0
        for letter in word:
            if not string_in_list(letter, checked_letters) and string_in_list(letter, letters_not_used):
                weighted_words[word] = weighted_words.get(word, 0) + 1
                checked_letters.append(letter)
    return weighted_words

def get_max_word(weighted_word: dict[str, int]) -> str:
    return max(weighted_word, key = lambda word: weighted_word[word])

def get_best_word(syllable: str, word_list: list[str], letters_not_used: list[str]) -> str:
    available_words: list[str] = get_all_available_words(syllable, word_list)
    weighted_words: dict[str, int] = weigh_word(available_words, letters_not_used)
    word = get_max_word(weighted_words)
    return word