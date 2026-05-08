def can_build_word(base_word, attempt_word):
    """
    Checks if submitted word can be made from the base word.

    Args:
        base_word (str): word for the round.
        attempt_word (str): word that player entered.

    Returns:
        bool: True if the word can be built from the base word,otherwise False.
    """
    base_letters = list(base_word.lower())

    for letter in attempt_word.lower():
        if letter in base_letters:
            base_letters.remove(letter)
        else:
            return False
        
    return True


def validate_player_words(base_word, submitted_words,word_list):
    """
    Checks the Player's submitted words for one round.
    This function check whether each word:
    1.is in the allowed word list 
    2.can be made from the base word
    3. is not repeated
    
    Args: 
    base_word(str): the main word used in the round
    submitted _words (list[str]):the words enterd by the player
    word_list(list[str]): a list od valid words for the game
    
    Returns: 
    dict: a dictionary with valid words,invalid words, duplcate and the total score for valid words
    """
    
    valid_words= []
    invalid_words= []
    duplicate_words= []
    used_words= set()
    total_score=0
    
    allowed_words = set()
    for word in word_list:
        allowed_words.add(word.lower().strip())
    
    base_word = base_word.lower().strip()
    
    for word in submitted_words:
        word = word.lower().strip()
        
        if word in used_words:
            duplicate_words.append(word)
            continue
        
        used_words.add(word)
        
        if word not in allowed_words:
            invalid_words.append(word)
            continue 
        
        if can_build_word(base_word, word):
            valid_words.append(word)
            total_score += len(word)
        else:
            invalid_words.append(word)

    return {
        "valid_words": valid_words,
        "invalid_words": invalid_words,
        "duplicate_words": duplicate_words,
        "score": total_score
    }

if __name__ == "__main__":
    sample_word_list = ["cat", "art", "rat", "tar", "tea", "eat", "teach", "each"]
    sample_submitted_list = ["cat", "art", "apple", "cat", "tea", "each"]

    result = validate_player_words("teacher", sample_submitted_list, sample_word_list)
    print(result)
    
