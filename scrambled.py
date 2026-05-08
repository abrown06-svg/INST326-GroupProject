import random
from collections import Counter
import nltk
nltk.download('words')
from nltk.corpus import words as nltk_words
from argparse import ArgumentParser

#One shared word list for entire game
dictionary = set(
    w.lower() for w in nltk_words.words()
    if w.isalpha() and 3 <= len(w) <= 12
)

'''
The computer_player checks whether a word can be formed from the base word and tests the letter count. Then it searches through two difficulties.
Difficulty Levels:
Easy: Chooses the shortest words
Hardest: Chooses the longest possible for the most points

Args: 
base_word(str): the word used in the round
difficulty (str): the difficulty level "easy" or "hard."

Returns:
tuple: a list of the words selected with a score based on the words created.
'''

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
    valid_words = [w for w in dictionary if can_form_word(base_word, w) and len(w) >= 4]    
    if difficulty == "easy":
        # Easy: pick up to 4 random short words
        choices = [w for w in valid_words if len(w) <= 4]
        computer_words = random.sample(choices, min(4, len(choices)))
    
    elif difficulty == "hard":
        # Hard: pick best-scoring words (longest) more room for points
        valid_words.sort(key=lambda w: len(w), reverse=True)
        computer_words = valid_words[:4]
    
    else:
        computer_words = []
    
    score = sum(score_word(w) for w in computer_words)
    
    return computer_words, score

def word_generator(file_words, difficulty):
    """
    Randomly selects and scrambles words based on difficulty for a given round. 
    Aswell as ensures the generated words can form at least three 
    valid dictionary words before selecting them. 
    Args:
        file_words (list[str]): List of all words loaded from the file.
        difficulty (str): Either "easy", or "hard".
    Returns:
    tuple[str, list[str]] | None:
        The selected base word and its scrambled letters,
        or None if no valid word could be generated.
    Side Effects:
        Randomly shuffles candidate word lists and scrambled letters.
    """
    
    filtered_words = [
        word.lower().strip()
        for word in file_words
        if 4<= len(word.strip()) <=12 and
        (
            (difficulty == "easy" and len(word) <= 6) or
            (difficulty == "hard" and len(word) > 6)
            
        )
    ]
                
    random.shuffle(filtered_words)
    for candidate in filtered_words:
        scrambled_words = list(candidate)
        random.shuffle(scrambled_words)
        
        possible_words_count = 0
        for dict_word in list(dictionary)[:2000]:
            if len(dict_word) >= 3:
                if can_form_word(candidate, dict_word):
                    possible_words_count += 1
            if possible_words_count >= 3:
                break
        
        if possible_words_count >= 3:
            return candidate, scrambled_words
    
    if filtered_words:
        fallback = random.choice(filtered_words)
        scrambled = list(fallback)
        random.shuffle(scrambled)
        return fallback, scrambled

    return None


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
    total_score= 0
    
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



def calculate_score(submitted_words, word_list, computer_words):
    """ 
        Calculates the total score for the user based on valid word submissions,
        word length, and bonus conditions.
        
        Args: 
            submitted_words (list): all guesses made 
            word_list (list): valid guesses 
            computer_words (list): words found by computer 
            
        Returns: int: total score for the user 
    """

    score = 0

    for word in set(submitted_words):

        if len(word) < 3:
            score -= 1
            continue

        if word not in word_list:
            score -= 1
            continue

        # base score
        length = len(word)

        points = 6 if length>=6 else length

        # bonus if computer didn't find it
        users_set = set(submitted_words)
        computers_set = set(computer_words)
        
        unique_words = users_set - computers_set
        
        if word in unique_words:
            points += 2

        # rare letter bonus
        for letter in word:
            if letter in "jyvzqx":
                points += 1
                break

        score += points

    #longest word comparison bonus (FIXED LOCATION)
    user_longest = ""
    for word in submitted_words:
        if word in word_list and len(word) > len(user_longest):
            user_longest = word

    computer_longest = ""
    for word in computer_words:
        if len(word) > len(computer_longest):
            computer_longest = word

    if len(user_longest) > len(computer_longest):
        score += 5

    return score

class WordGame:
    """
    Manages the overall game state and gameplay.

    Attributes:
        dictionary (set[str]): valid game words
        difficulty (str): selected difficulty level
        base_word (str | None): word used for current round
        scrambled (list[str] | None): shuffled letters
        submitted_words (list[str]): player guesses
        computer_words (list[str]): computer generated words
        player_score (int): player's score
        computer_score (int): computer's score
    
    """
    def __init__(self, dictionary, difficulty="easy"):
        self.dictionary = dictionary
        self.difficulty = difficulty
        self.base_word = None
        self.scrambled = None
        self.submitted_words = []
        self.computer_words = []
        self.player_score = 0
        self.computer_score = 0
        
    def generate_word(self):
        """
        Generates the word and scrambled letters using word_generator function
        """
        result = word_generator(list(self.dictionary), self.difficulty)
        if result:
            self.base_word, self.scrambled = result
            return True
        return False
    
    def play_computer_turn(self):
        """
        Computer finds words and calculates score using computer_player function
        """
        self.computer_words, self.computer_score = computer_player(
            self.base_word, 
            self.difficulty
        )
    
    def validate_words(self):
        """
        Validate player's submitted words using validate_player_words function
        """
        return validate_player_words(
            self.base_word, 
            self.submitted_words, 
            self.dictionary
        )
    
    def calculate_player_score(self, valid_words):
        """
        Calculate the player's final score using calculate_score function
        """
        self.player_score = calculate_score(
            valid_words, 
            self.dictionary, 
            self.computer_words
        )
        return self.player_score
    
    def display_results(self, validation_result):
        """Display the game results"""
        print("\n" + "=================")
        print("      ROUND RESULTS")
        print("=================")
        print(f"The Base word was: {self.base_word}")
        print()
        
        print("--- YOUR STATS ---")
        print(f"Valid words    : {validation_result['valid_words']}")
        if validation_result['invalid_words']:
            print(f"Invalid words  : {validation_result['invalid_words']}")
        if validation_result['duplicate_words']:
            print(f"Duplicates     : {validation_result['duplicate_words']}")
        print(f"Your score     : {self.player_score}")
        
        print()
        print("--- COMPUTER STATS  ---")
        print(f"Computer words : {self.computer_words}")
        print(f"Computer score : {self.computer_score}")
        print()
        print("=================")
        
        if self.player_score > self.computer_score:
            print(f"   YOU WIN! ({self.player_score} vs {self.computer_score})")
        elif self.computer_score > self.player_score:
            print(f"   COMPUTER WINS! ({self.computer_score} vs {self.player_score})")
        else:
            print(f"   TIE! ({self.player_score} vs {self.computer_score})")
        print("=================")

def main():
    """   
    Main program entry point.

    Parses difficulty from command line arguments,
    initializes the game, collects player input,
    runs the computer turn, calculates scores,
    and displays round results.
    """ 

    parser = ArgumentParser()
    parser.add_argument("difficulty")
    args = parser.parse_args()
    
    difficulty = args.difficulty
    game = WordGame(dictionary, difficulty)


    if not game.generate_word():
        print("Failed to generate word")
        exit()
    

    print("Scrambled letters:", " ".join(game.scrambled))
    
    while True:
        word = input("Enter Word: ")
        
        if word == "":
            break
        
        game.submitted_words.append(word)

    game.play_computer_turn()
    
    validation_result = game.validate_words()
    game.calculate_player_score(game.submitted_words)
    
    game.display_results(validation_result)
    
if __name__ == "__main__":
    main()
    
