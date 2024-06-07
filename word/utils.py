import random

def get_weight(word: str, letters_not_used: list[str]) -> int:
    """Get weight for word based on letters not used

    Args:
        word (str): Word to get weight for
        letters_not_used (list[str]): List of letters not used

    Returns:
        int: Weight based on letters not used
    """
    checked_letters: set = set()
    return sum(1 for letter in word if letter in letters_not_used and (letter not in checked_letters and not checked_letters.add(letter)))

def get_all_available_words(syllable: str, word_list: set, max_length: int = 0, min_length: int = 0, fallback = True) -> set[str]:
    """Returns all available words and optionally checks for length

    Args:
        syllable (str): Syllable to search for
        word_list (set[str]): Words list to search through
        max_length (int, optional): Maximum length of word. Defaults to 0.
        min_length (int, optional): Minimum length of word. Defaults to 0.
        fallback (bool, optional): Discards word length requirements if none found. Defaults to True.

    Returns:
        set: List of available words
    """
    check_max, check_min = max_length > 0, min_length > 0
    available = set([word for word in word_list if syllable in word and (not check_min or len(word) >= min_length) and (not check_max or len(word) <= max_length)])
    return available if len(available) > 0 or not (check_min or check_max) or not fallback else get_all_available_words(syllable, word_list)

def weigh_words(available_words: set[str], letters_not_used: list[str]) -> dict[str, int]:
    """Returns dictionary of words and their weights based on letters not used

    Args:
        available_words (set[str]): List of available words
        letters_not_used (list[str]): List of letters not used

    Returns:
        dict[str, int]: Dictionary of words and their weights based on letters not used
    """
    return {word: get_weight(word, letters_not_used) for word in available_words}
    
def get_max_word(weighted_words: dict[str, int]) -> str:
    """Returns word with max weight given weighted words

    Args:
        weighted_words (dict[str, int]): Dictionary of weighted words

    Returns:
        str: Word with max weight
    """
    return max(weighted_words, key = lambda word: weighted_words[word])

def get_best_word(syllable: str, word_list: set[str], letters_not_used: list[str], max_length: int = -1, min_length: int = 0) -> str:
    """Gets best word based on letters not used

    Args:
        syllable (str): Syllable to search for
        word_list (set[str]): Word list to search through
        letters_not_used (list[str]): List of letters not used
        max_length (int, optional): Maximum length of word. Defaults to -1.
        min_length (int, optional): Minimum length of word. Defaults to 0.

    Returns:
        str: Best word based on letters not used
    """
    return get_max_word(weigh_words(get_all_available_words(syllable, word_list, max_length, min_length), letters_not_used))

def get_random_available_word(syllable: str, word_list: set[str], max_length: int = 0, min_length: int = 0) -> str:
    """Get random word given syllable

    Args:
        syllable (str): Syllable to search for
        word_list (set[str]): List of words to search through
        max_length (int, optional): Maximum length of word. Defaults to 0.
        min_length (int, optional): Minimum lenght of word. Defaults to 0.

    Returns:
        str: Random word given syllable
    """
    return random.choice(get_all_available_words(syllable, word_list, max_length, min_length))

def get_longest_word(syllable: str, word_list: set[str]) -> str:
    """Get longest word given syllable

    Args:
        syllable (str): Syllable to search for
        word_list (set[str]): Word list to search through

    Returns:
        str: Longest word given syllable
    """
    available_words: set[str] = get_all_available_words(syllable, word_list)
    return max(available_words, key = lambda word: len(word))