# Scrambled
### Scrambled is a game that takes a random word from a dictionary (word library) and a player must go against a computer in easy or hard more. You are appointed a score based on the length of the words found and if you use special characters. Additionally, if you find a word the computer didn't find, you get +2 points.

## How to Run

Run the game from the command line with a difficulty level:

`python3 scrambled.py easy` or `python3 scrambled.py hard`

Requirement: `nltk`

## Files

- `scrambled.py` → main game loop
- `ahmadsword_generator.py` → word generator and difficulty filtering
- `ashleyvalidatewords.py` → player word validation system
- `kayssyscoring.py` → scoring system
- `xandercomputerfunction.py` → computer player system

---

## Ahmad Brown

functions:
- `word_generator`

what it does:
- generates scrambled letters based on difficulty
- filters words by length and difficulty
- uses the NLTK word library

claimed techniques:
- randomization
- iteration
- conditional branching
- external library usage

---

## Chang Liu / Ashley

functions:
- `validate_player_words`

what it does:
- checks if submitted words are valid
- checks if words can be made from the base word
- tracks duplicate, valid, and invalid words

claimed techniques:
- iteration
- conditional branching
- lists and dictionaries
- input validation

---

## Kayssy Kengne

functions:
- `calculate_score`

what it does:
- calculates the player score
- gives points based on word length
- adds bonus points for rare letters
- adds bonus points if the player finds a word the computer did not find

claimed techniques:
- iteration
- conditional branching
- set usage
- scoring logic

---

## Xander Boyko

functions:
- `computer_player`
- `can_form_word`

what it does:
- creates the computer player’s word choices
- uses easy mode for shorter words
- uses hard mode for longer words
- returns the computer words and score

claimed techniques:
- Lambda Expressions
- List Comphrensions

---

## Challenges
...

## Live Demo

The demo will show:
- choosing easy or hard difficulty
- generating scrambled letters
- entering player words
- showing the computer’s words
- comparing the final scores

If there is time, we can ask the class to suggest one word during the demo.
