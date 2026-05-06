# Scrambled
Scrambled is a game that takes a random word from a dictionary, scrambles the letters, and a player must go against a computer in easy or hard mode, tries to make as many valid words as possible from the scrambled letters.

You are appointed a score based on the length of the words found and can get bonus points for using rare letters. Additionally, if you finds a word the computer did not find, you will get 2 points.

Try to get a higher score than the computer by the end of the game!

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

components:
- `word_generator` function
- `WordGame Class`
- `main program`

what it does:
- generates scrambled letters based on difficulty
- makes sure the round has playable word combinations
- list comprehension used to filter and transform word list based on length and difficulty
- uses the NLTK word library
- manages overall game state including player input and scores
- handles command line input for difficulty selection

claimed techniques:
- list comprehension
- the ArgumentParser class from the argparse module

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

components:
- `computer_player` function
- `can_form_word` function
- `WordGame Class`

what it does:
- creates the computer player’s word choices
- uses easy mode for shorter words
- uses hard mode for longer words
- returns the computer words and score
- displays results of game

claimed techniques:
- Lambda Expressions
- F Strings

---


## Live Demo

The demo will show:
- choosing easy or hard difficulty
- generating scrambled letters
- entering player words
- showing the computer’s words
- comparing the final scores

If there is time, we can ask the class to suggest one word during the demo.
