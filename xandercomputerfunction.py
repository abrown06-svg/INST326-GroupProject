import random
from collections import Counter
'''
The computer function checks whether a word can be formed from the base word and tests the letter count. Then it searches through two difficulties.
The computer can select up to 4 words.
Difficulty Levels:
Easy: Chooses the shortest words
Hardest: Chooses the longest possible for the most points

Args: 
base_word(str): the word used in the round
difficulty (str): the difficulty level "easy" or "hard."

Returns:
tuple: a list of the words selected with a score.
'''
# Sample to show an example
WORD_LIST = [
    "cat", "dog", "tire", "tar", "art", "car", "arc",
    "race", "pace", "tower", "tape", "ape", "tap",
    "tune", "knife", "cute", "chute", "teach", "eating", "tea"
]

# Verify if words can be generated from the word list
def can_form_word(base_word, attempt_word):
    base_count = Counter(base_word.lower())
    test_count = Counter(attempt_word.lower())
    
    for letter in test_count:
        if test_count[letter] > base_count.get(letter, 0):
            return False
    return True

# Score function (simple: length = points)
def score_word(word):
    return len(word)

# Computer player function
def computer_player(base_word, difficulty="easy"):
    valid_words = [w for w in WORD_LIST if can_form_word(base_word, w)]
    
    if difficulty == "easy":
        # Easy: pick up to 4 random short words
        choices = [w for w in valid_words if len(w) <= 4]
        computer_words = random.sample(choices, min(4, len(choices)))
    
    elif difficulty == "hard":
        # Hard: pick best scoring words (longest)
        valid_words.sort(key=lambda w: len(w), reverse=True)
        computer_words = valid_words[:4]
    
    else:
        computer_words = []
    
    score = sum(score_word(w) for w in computer_words)
    
    return computer_words, score
