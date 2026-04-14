import random
import nltk
nltk.download('words')
from nltk.corpus import words as nltk_words

def word_generator(file_words, difficulty):
    """
    Randomly selects and scrambles words based on difficulty for a given round. 
    Args:
        file_words (list[str]): List of all words loaded from the file.
        difficulty (str): Either "easy", or "hard".
    Returns:
        list[str]: Letters selected for the round, shuffled into random order.
    """
    
    dictionary = set(w.lower() for w in nltk_words.words())
    
    min_letters = 4
    max_letters = 12
    
    filtered_words = []
    for word in file_words:
        word = word.lower().strip()
        if 4<= len(word) <=12:
            if difficulty == "easy" and len(word) <= 6:
                filtered_words.append(word)
            elif difficulty == "hard" and len(word) > 6:
                filtered_words.append(word)
                
    random.shuffle(filtered_words)
    for candidate in filtered_words:
        scrambled_words = list(candidate)
        random.shuffle(scrambled_words)
        
        possible_words_count = 0
        for dict_word in dictionary:
            if len(dict_word) >= 4:
                if all(letter in candidate for letter in dict_word):
                    possible_words_count += 1
            if possible_words_count >= 3:
                break
        
        if possible_words_count >= 3:
            return(scrambled_words)
    
    return []
