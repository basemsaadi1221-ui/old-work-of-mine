import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while "_" in words or " " in words:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    word = get_valid_word(words)
    word_letters = set(word)
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("you have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        word_list = []
        for letters in word:
            if letters in used_letters:
                word_list.append(letters)
            else:
                word_list.append("-")
        print("current word: "," ".join(word_list))

        user_letters = input("Guess a letter: ").upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print("")
            else:
                lives = lives - 1
                print("\nYour letter,", user_letters, "is not in the word.")

        elif user_letters in used_letters:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("\nThat is not a valid letter.")

    if lives == 0:
        print("you died, sorry. the word was: ", word)
    else:
        print("YAY! You guessed the word", word, "!!")

hangman()