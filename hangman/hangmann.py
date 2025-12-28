import random
import string
from words import words

def get_vald_word():
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangmann():
    word = get_vald_word()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("you have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)        # Show the letter
            else:
                word_list.append("-")
                
        print("current word: ", " ".join(word_list))

        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print("\n YAY! your letter,", user_letters, "is in the word")

            else:
                lives = lives - 1                   # takes away a life if wrong
                print("\nYour letter,", user_letters, "is not in the word.")

        elif user_letters in used_letters:
            print("\n you already used,", user_letters, "befor guess another letter")

        else:
            print("\n That is not a valid letter")

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

hangmann()

        