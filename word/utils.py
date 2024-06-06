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

def get_all_available_words(syllable: str, word_list: list[str], max_length: int = -1, min_length: int = 0) -> list[str]:
    """Get all words that have syllable in them

    Args:
        syllable (str): Syllable to search for
        word_list (list[str]): Words to search through
        max_length (int, optional): Maximum word length. Defaults to -1.
        min_length (int, optional): Minimum word length. Defaults to 0.

    Returns:
        list[str]: List of all words that have syllable in them
    """
    check_length: bool = False if max_length == -1 else True
    
    available: list[str] = []
    
    for word in word_list:
        if substring_in_string(syllable, word):
            if not check_length or min_length <= len(word) <= max_length:
                available.append(word)
    
    if check_length and len(available) == 0:
        available = get_all_available_words(syllable, word_list)
    elif len(available) == 0:
        available = ['404']
    
    return available
                
def get_random_available_word(syllable: str, word_list: list[str], max_length: int = -1, min_length: int = 0) -> str:
    """Get random word that has syllable in it

    Args:
        syllable (str): Syllable to search for
        word_list (list[str]): Words to search through
        max_length (int, optional): Maximum word length. Defaults to -1.
        min_length (int, optional): Minimum word length. Defaults to 0.

    Returns:
        str: Random word with syllable in it
    """
    available: list[str] = get_all_available_words(syllable, word_list, max_length, min_length)
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

def get_best_word(syllable: str, word_list: list[str], letters_not_used: list[str], max_length: int = -1, min_length: int = 0) -> str:
    available_words: list[str] = get_all_available_words(syllable, word_list, max_length, min_length)
    weighted_words: dict[str, int] = weigh_word(available_words, letters_not_used)
    word = get_max_word(weighted_words)
    return word