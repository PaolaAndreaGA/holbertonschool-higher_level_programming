#!/usr/bin/python3
import random

stage = \
    '''   
~~~~~~~~~|~
         |
   0123456 
~~~~~~~~~~   
'''

symbols = '>--|x:p'




def welcome():
    print ('*' * 68)
    print ('* Welcome to the hangman game *')
    print ('*' * 68)


def initialize_game(dictionary):
    word = random.choice(dictionary).lower()
    board = ['_'] * len(word)
    return board, word, []


def show_stage(error):
    scene = stage
    for i in range (0, len (symbols)):
        symbol = symbols[i] if i < error else ''
        scene = scene.replace(str(i), symbol)
    print(scene)

def show_board(board, wrong_letters):
    for box in board:
        print(box, end = '')
    print()
    print()
    if len(wrong_letters)> 0:
        print('Wrong letters:', *wrong_letters)
        print()

def ask_letter(board, wrong_letters):
    valid = False
    while not valid:
        letter = input('Enter a letter (a-z):').lower ()
        valid = 'a' <= letter <= 'z' and len(letter) == 1 
        if not valid:
            print('Error, the letter must be between a and z')
        else:
            valid = letter not in board + wrong_letters
            if not valid:
                print('Repeated letter, try another')

    return letter


def process_letter(letter, word, board, wrong_letters):
    if letter in word:
        print('Great! You got a letter right.')
        update_board(letter, word, board)
    else:
        print('Oh! You failed.')
        wrong_letters.append(letter)


def update_board(letter, word, board):
    for index, letter_word in enumerate(word):
        if letter == letter_word:
            board[index] = letter


def check_word(board):
    return '_' not in board


def play_hangman(dictionary):

    board, word, wrong_letters = initialize_game(dictionary)
    while len(wrong_letters) < len(symbols):
        show_stage(len(wrong_letters))
        show_board(board, wrong_letters)
        letter = ask_letter(board, wrong_letters)
        process_letter(letter, word, board, wrong_letters)
        if check_word(board):
            print('Congratulations, you did it!')
            break
    else:
        print('Sorry! You lost! The word to guess was {word}')
        show_stage(len(wrong_letters))

    show_board(board, wrong_letters)


def play_again():
    return input('Do you want to play again enter y for yes or n for no):')


def fired():
    print ('*' * 68)
    print ('* Thanks for playing Hangman from See you soon! *')
    print ('*' * 68)


if __name__ == '__main__':

    dictionary = ['house', 'bedroom', 'window', 'door', 'table']

    welcome()
    while True:
        play_hangman(dictionary)
        if play_again()!= 'y': break
    fired()
