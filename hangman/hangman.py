from random import choice
from string import ascii_lowercase


def play():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = choice(word_list)
    letters = set(word)
    letter_attempts = set()
    hint = list('-' * len(word))
    attempts = 8
    while attempts > 0:
        print()
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) > 1:
            print("You should input a single letter")
        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in letter_attempts:
            print("You already typed this letter")
        else:
            letter_attempts.add(letter)
            if letter in letters:
                pos = -1
                while True:
                    pos = word.find(letter, pos + 1)
                    if pos == -1:
                        break
                    hint[pos] = letter
            else:
                attempts -= 1
                print("No such letter in the word")

    if attempts > 0 and hint.find('-') != -1:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")


def menu():
    print("H A N G M A N")

    while True:
        action = input("Type \"play\" to play the game, \"exit\" to quit:")
        if action == "play":
            play()
        elif action == "exit":
            break


if __name__ == "__main__":
    # execute only if run as a script
    menu()