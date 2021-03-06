import random

word_list = []
guess_list = []
wrong_list = []

with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        stripped = line.strip('\n').upper()
        word_list.append(stripped)

def easy_words(words):
    easy_list = []
    for string in words:
        if len(string) >= 4 and len(string) <= 6:
            easy_list.append(string)
    return easy_list

def medium_words(words):
    medium_list = []
    for string in words:
        if len(string) >= 6 and len(string) <= 8:
            medium_list.append(string)
    return medium_list

def hard_words(words):
    hard_list = []
    for string in words:
        if len(string) >= 8:
            hard_list.append(string)
    return hard_list

def select_list(difficulty):
    if difficulty == 'E':
        return easy_words(word_list)
    if difficulty == 'N':
        return medium_words(word_list)
    if difficulty == 'H':
        return hard_words(word_list)
    if difficulty not in ['E', 'N', 'H']:
        print("Please only enter 'E', 'N', or 'H'")
        dif = input("Please only: [E]asy [N]ormal or [H]ard: ").upper()
        return select_list(dif)

def random_word(difficulty):
    return random.choice(difficulty)

def get_guess():
    return input("Please guess a letter: ").upper()

def check_guess(guess):
    if len(guess) > 1:
        print("That isn't a good guess!")
        return False
    if guess not in guess_list:
        guess_list.append(guess)
        return True
    else:
        print("You already guessed that!")
        return False

def is_guess_in_secret(secret, guess):
    if guess not in secret:
        if guess not in wrong_list:
            wrong_list.append(guess)
        return False
    else:
        return True

def display_word(secret, guess_list):
    board = []
    if board == []:
        for letter in secret:
            board.append("_")
    for idx, letter in enumerate(list(secret)):
        if letter in guess_list:
            board[idx] = letter.upper()
    return ' '.join(board)

def is_word_complete(secret, guess):
    for letter in secret:
        if letter not in guess:
            return False
    return True

def game_over():
    ask = input("Do you want to play again? [Y]es or [N]o").upper()
    if ask == 'Y':
        del guess_list[:]
        del wrong_list[:]
        return True
    if ask == 'N':
        exit(0)
    else:
        print("Please enter 'Y' or 'N'")

def out_of_rounds(secret):
    print("You ran out of rounds! The secret word was {}.".format(secret))

def main():
    round_counter = 1
    difficulty = input("Play the game! [E]asy [N]ormal or [H]ard: ").upper()
    difficulty = select_list(difficulty)
    secret = random_word(difficulty)
    print(secret)
    while round_counter < 9:
        print("Round: ", round_counter)
        round_counter += 1
        guess = get_guess()
        if check_guess(guess):
            if is_guess_in_secret(secret, guess):
                print(display_word(secret, guess_list))
                round_counter -= 1
            else:
                print(display_word(secret, guess_list))
        else:
            round_counter -= 1
        print("Wrong Letters: ", wrong_list)
        if is_word_complete(secret, guess_list):
            print("You saved the hanging human!")
            if game_over():
                main()
                break
    out_of_rounds(secret)

if __name__ == "__main__":
    main()
