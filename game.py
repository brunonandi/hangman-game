import os
import secrets
from unidecode import unidecode


def main():
    while True:
        option = input("Select an option: ")

        if option == "1":
            easy()
            break

        elif option == "2":
            normal()
            break

        elif option == "3":
            hard()
            break

        elif option.upper() == "Q":
            break

        else:
            print("Invalid Option. Choose another!")


def easy():
    selected_word, normalized_word = choose_word("easy_words.txt")
    attempts = 5
    request_guesses(word=selected_word, comparison_word=normalized_word,
                    attempts_remaining=attempts)


def normal():
    selected_word, normalized_word = choose_word("normal_words.txt")
    attempts = 4
    request_guesses(word=selected_word, comparison_word=normalized_word,
                    attempts_remaining=attempts)


def hard():
    selected_word, normalized_word = choose_word("hard_words.txt")
    attempts = 3
    request_guesses(word=selected_word, comparison_word=normalized_word,
                    attempts_remaining=attempts)


def choose_word(filename):
    words_list = list(line.rstrip() for line in open(filename))
    selected_word = secrets.choice(words_list)
    normalized_word = unidecode(selected_word)

    return selected_word.upper(), normalized_word.upper()


def request_guesses(word, comparison_word, attempts_remaining):
    clear_terminal()
    secret_word = ["_" for i in word]
    guesses_list = list()

    while attempts_remaining > 0:
        print_info(attempts_remaining=attempts_remaining,
                   guesses_list=guesses_list, secret_word=secret_word)

        guess = input("Your shot: ").upper()
        valid = (guess.isalpha() and len(guess) == 1)

        if valid:
            if guess in comparison_word:
                for i, c in enumerate(comparison_word):
                    if guess == c:
                        secret_word[i] = c

            else:
                attempts_remaining -= 1

            guesses_list.append(guess)

            full_secret_word = "".join(secret_word)

            if full_secret_word == comparison_word:
                congratulations(word=word)
                break

        else:
            print("Invalid! Try again!")

    clear_terminal()
    print("So sad! Try again!\n")
    print(f"The word was {word}")


def congratulations(word):
    print("CONGRATULATIONS!!! \nYOU WIN!!!")


def print_info(attempts_remaining, guesses_list, secret_word):
    clear_terminal()
    normalized_secret_word = "".join(secret_word)
    normalized_guesses_list = ", ".join(guesses_list)
    print(
        f"The word has {len(secret_word)} letters: {normalized_secret_word}")
    print(f"\nAttempts Remaining: {attempts_remaining}")
    print(f"\nGuesses: {normalized_guesses_list}")
    print("-"*30)


def clear_terminal():
    os.system("clear")


if __name__ == "__main__":
    print("""
    ***************************
    * WELCOME TO HANGMAN GAME *
    ***************************

    Options:
        [1] Easy       (5 attempts)
        [2] Normal     (4 attempts)
        [3] Hard       (3 attempts)
        [Q] Quit Game
    """)

    main()
