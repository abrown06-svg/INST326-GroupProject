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
    used_words= []
    total_score=0
    
    base_word = base_word.lower()
    
    for word in submitted_words:
        word = word.lower().strip()
        
        if word in used_words:
            duplicate_words.append(word)
            continue
        
        used_words.append(word)
        
        if word not in word_list:
            invalid_words.append(word)
            continue 
        
        base_letters = list(base_word)
        can_make_word = True
        
        for letter in word:
            if letter in base_letters:
                base_letters.remove(letter)
            else:
                can_make_word = False
                break
            
        if can_make_word:
            valid_words.append(word)
            total_score += len(word)
        else:
            invalid_words.append(word)
    
    return{
        "valid_words": valid_words,
        "invalid_words": invalid_words,
        "duplicate_words": duplicate_words,
        "score":total_score
    }    

sample_word_list =["cat","art","rat","tar","tea","eat","teach"]
sample_submitted_list = ["cat","art","apple","cat","tea"]

result = validate_player_words("teacher",sample_submitted_list,sample_word_list)
print(result)
