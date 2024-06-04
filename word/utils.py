def substring_in_string(substring: str, full_string: str) -> bool:
    return substring.lower() in full_string.lower()

def get_all_available_words(syllable: str, word_list: list[str], min_length: int = -1, max_length: int = -1) -> list[str]:
    check_length: bool = False if min_length == -1 and max_length == -1 else True
    
    available: list[str] = []
    
    for word in word_list:
        if substring_in_string(syllable, word):
            if not check_length or min_length <= len(word) <= max_length:
                available.append(word)