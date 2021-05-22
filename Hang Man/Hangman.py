import random
import string
from Words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 9
    while len(word_letters) > 0:
        #Lives
        print(f'Lives Left: {lives}')

        #Letters Used
        print(f'Used Letters: {used_letters}')

        #Correct Word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f'Correct Word: {word_list}')

        #Game Details
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"The letter {user_letter} is in the word. Keep it Up!\n")
            else:
                lives = lives - 1
                print(f"This letter is not in the word! You have {lives} lives left!\n")
        elif user_letter in used_letters:
            print(f"You have already used {user_letter}. Please Try another letter\n")
        else:
            print('Invalid Character\n')

        #Checking for Lives
        if lives == 0:
            print("Game Over! Try Again!")
            break
    print(f"The word is {word}")

Play = "A"
while Play != 'Y' or 'N':
    Play = input("Do you wanna play hangman? (Y/N)").upper()
    if Play == 'Y':
        print(hangman())
        break
    if Play == 'N':
        print('See you again!')
        break
    elif Play != 'N' or 'Y':
        print ("Choose btwn Y/N")