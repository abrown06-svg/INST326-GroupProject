def calculate_score(submitted_words, word_list, computer_words):

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

        if length == 3:
            points = 3
        elif length == 4:
            points = 4
        elif length == 5:
            points = 5
        else:
            points = 6

        # bonus if computer didn't find it
        if word not in computer_words:
            points += 2

        # rare letter bonus
        for letter in word:
            if letter in "jyvzqx":
                points += 1
                break

        score += points

    # 🔥 longest word comparison bonus (FIXED LOCATION)
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

word_list = [
    "chute",
    "catch",
    "cure",
    "pure",
    "race",
    "teach",
    "reach",
    "trace",
    "chart",
    "hat",
    "rat",
    "cat",
    "tea",
    "cue",
    "ape",
    "area",
    "cute"
]
submitted_words = [
    "chute",
    "race",
    "cat",
    "teach",
    "ape"
]

computer_words = [
    "catch",
    "cure",
    "pure",
    "tea",
    "reach"
]

score = calculate_score(submitted_words, word_list, computer_words)
print(score)