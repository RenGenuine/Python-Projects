import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # chooses random word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    tries = 6

    # getting user input
    while len(word_letters) > 0 and tries > 0: # while there's still LETTERS to guess AND there's still TRIES left
        # used letters
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', tries, ' tries left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (Ex: W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] # substitutes unused letters for "-"
        print('Current word: ', ' '.join(word_list))



        guessed_letter = input('Guess a letter: ').upper()
        if guessed_letter in alphabet - used_letters: # if guessed letter is in remaining letters
            used_letters.add(guessed_letter) # add guessed letter to the list of used ones
            if guessed_letter in word_letters: # and if guessed letter is in the word set
                word_letters.remove(guessed_letter) # remove guessed letter from the word set
            
            else:
                tries = tries - 1 # removes a try if wrong
                print("Wrong choice.")

        elif guessed_letter in used_letters: # if guessed letter is already used
            print('You have already used that letter. Try again')

        else: # if they type something other than a letter
            print("Invalid character. Try a letter instead.")
    
    if tries == 0:
        print("Sorry, you lose...")
    print(word)
    print ("You guessed the right word! Good job!")        

hangman()
user_input = input('Guess the word by typing a letter:')


