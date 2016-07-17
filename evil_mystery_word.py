import random
import operator

word_list = []
length_word_list = []
guess_list = []
wrong_guesses = []
board = []

with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        stripped = line.strip('\n').upper()
        word_list.append(stripped)

def get_length():
    try:
        length = int(input("Pick a word length between 1 and 24 letters: "))
        lengths = {}
        for item in word_list:
            lengths[len(item)] = 1
        if length not in lengths:
            print("There are no words of this length in our dictionary!")
            get_length()
        elif length < 1 or length > 24:
            print("Please... pick a number between 1 and 24: ")
            get_length()
        return length
    except ValueError:
        print("Not a number!")
        get_length()

def make_length_word_list(length):
    for item in word_list:
        if len(item) == length:
            length_word_list.append(item)
    return length_word_list

def get_rounds():
    try:
        rounds = int(input("How many guesses do you want? "))
        if rounds < 1:
            print("Please... pick a integer greater than 0: ")
            get_rounds()
        return rounds
    except ValueError:
        print("Not a number!")
        get_rounds()

def want_word_list_length():
    response = input("Do you want to know the number of possible words remaining? [Y]es or [N]o? ").upper()
    if response != 'Y' and response != 'N':
        print("Please only input 'Y' or 'N'.")
        want_word_list_length()
    return response == 'Y'

# I found this potential solution to making famalies of lists, but I don't quite
# Understand... will ask Bryce or Sam.  Specifically line 51
# from itertools import groupby
#
# words = ['ALLY', 'BETA', 'COOL', 'DEAL', 'ELSE', 'FLEW', 'GOOD', 'HOPE', 'IBEX']
# e_locs = sorted(([c == 'E' for c in w], i) for i, w in enumerate(words))
# result = [[words[i] for x, i in g] for k, g in groupby(e_locs, lambda x: x[0])]

#Returns dictionary based on guess and letter position
def partition_word_list(guess, wrdlst):
    families = {}
    for word in wrdlst:
        fltr = ''.join(guess if letter == guess else '-' for letter in word)
        if fltr not in families:
            families[fltr] = []
        families[fltr].append(word)
    return families

#Returns tuple of the dictionary item with the longest list of words
def longest_family_tuple(families):
    return max(families.items(), key=lambda k_v: len(k_v[1]))

#Appends to length_word_list (our updated word list) the longest list from partition
def update_list(a_tuple):
    del length_word_list[:]
    for item in a_tuple[1]:
        length_word_list.append(item)

def compare_display_to_board(a_tuple, board, guess):
    if board == []:
        for letter in list(a_tuple[0]):
            board.append(letter)
        print("1")
    if list(a_tuple[0]) == list('-'*len(board)):
        print("You missed!")
        print("2")
        wrong_guesses.append(guess)
    else:
        for idx, letter in enumerate(list(a_tuple[0])):
            if letter != board[idx]:
                if board[idx] == '-':
                    board[idx] = letter
        print("3")
    print(' '.join(board))

def word_list_length(wrdlst):
    return len(wrdlst)

def get_guess():
    return input("Please guess a letter: ").upper()

def check_guess(guess):
    if len(guess) > 1 or len(guess) <= 0:
        print("That isn't a good guess!")
        return False
    if guess not in guess_list:
        guess_list.append(guess)
        return True
    else:
        print("You already guessed that!")
        return False

def game_over():
    ask = input("Do you want to play again? [Y]es or [N]o").lower()
    if ask == 'y':
        del guess_list[:]
        del wrong_guesses[:]
        del board[:]
        main()
    if ask == 'n':
        exit(0)
    else:
        print("Please enter 'Y' or 'N'")

def out_of_rounds(secret):
    print("You ran out of rounds! The secret word was {}.".format(random.choice(length_word_list)))

def main():
    length = get_length()
    make_length_word_list(length)
    rounds = get_rounds()
    want_list_length = want_word_list_length()
    while rounds > 0:
        if want_list_length:
            print("# of Words Left: ", word_list_length(length_word_list))
        print("Guesses Remaining: ", rounds)
        print("Wrong Guesses: ", ' '.join(wrong_guesses))
        guess = get_guess()
        rounds -= 1
        if check_guess(guess):
            partitioned = partition_word_list(guess, length_word_list)
            longest_family = longest_family_tuple(partitioned)
            update_list(longest_family)
            compare_display_to_board(longest_family, board, guess)
            if guess in board:
                rounds += 1
            for letter in board:
                if '-' not in board:
                    print("You won... somehow")
                    game_over()
        else:
            rounds += 1
    out_of_rounds(length_word_list)

if __name__ == "__main__":
    main()
