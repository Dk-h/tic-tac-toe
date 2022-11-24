
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

import random
import os

def clear_output():
    os.system('cls')
    print_TicTacToe()

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

def display_board(board):
    print(f'''
       |       |
   {board[0]}   |   {board[1]}   |   {board[2]}
_______|_______|_______
       |       |
   {board[3]}   |   {board[4]}   |   {board[5]}
_______|_______|_______
       |       |
   {board[6]}   |   {board[7]}   |   {board[8]}
       |       |
       ''')

# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

def player_input():
    deal = True

    details_of_players=None

    player1_name = input("Player 1 enter your name : ")
    while deal:
        choice = input("Choose any one 'X' or 'O' : ").upper()
        if choice.lower() == 'x' or choice.lower() == 'o':
            deal = False
        else:
            print('Invalid Input!\nTry Again!')

    # color_of_p1 = input('Which colour do you like?:') 

    clear_output()

    player2_name = input("Player 2 enter your name : ")
    # color_of_p2 = input('Which colour do you like?:')

    print(f'\n{player1_name} has choosen {choice}\nAnd {player2_name} has been appointed',
          'O' if choice.upper() == 'X' else 'X')

    first = choose_first()

    p1_marker = choice
    p2_marker = ('O' if choice == 'X' else 'X')

    if first == 0:
        name_of_who_plays_first = player1_name
        name_of_who_plays_second = player2_name
        details_of_players={'who_plays_first': {'name': name_of_who_plays_first, 'marker': p1_marker},
                            'who_plays_second': {'name': name_of_who_plays_second, 'marker': p2_marker}}
    else:
        name_of_who_plays_first = player2_name
        name_of_who_plays_second = player1_name
        details_of_players={'who_plays_first': {'name': name_of_who_plays_first, 'marker': p2_marker},
                            'who_plays_second': {'name': name_of_who_plays_second, 'marker': p1_marker}}

    print(f'\n{name_of_who_plays_first} plays first')
    
    os.system('pause')

    return details_of_players

# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

def place_marker(board, marker, position):
    board[position] = marker

# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

def win_check(board, mark):

    return(
        (board[0] == mark and board[1] == mark and board[2] == mark) or
        (board[3] == mark and board[4] == mark and board[5] == mark) or
        (board[6] == mark and board[7] == mark and board[8] == mark) or

        (board[0] == mark and board[3] == mark and board[6] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or

        (board[0] == mark and board[4] == mark and board[8] == mark) or
        (board[2] == mark and board[4] == mark and board[6] == mark)
    )

# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

def choose_first():
    return random.randint(0, 1)

# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

def full_board_check(board):
    for values in board:
        if values != ' ':
            continue
        else:
            return False
    return True

# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

def player_choice(board):

    while True:
        index = int(input('Enter a number between 1-9 : '))
        if(index in range(1, 10)):
            if(space_check(board, index)):
                return index
                # will exit after returning
            else:
                print('Space already filled!')
                continue
        else:
            print('Number should be in the range 1-9')
            continue

# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

def replay():
    run = input("Play again if you enjoyed (Yes/No) : ")
    return run.lower() == 'yes'

def print_TicTacToe():
    print('''
████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗██╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝██║
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  ██║
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  ╚═╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗██╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝╚═╝
''')

def disco_light():
    import os
    import time
    from random import shuffle
    repeat = 0

    color = list(range(0, 10))
    shuffle(color)

    for ran in color:
        os.system('cls')
        os.system('color '+str(ran))
        print_TicTacToe()
        time.sleep(0.155)
        repeat += 1
        if repeat == 5:
            break
        else:
            continue

def entering_position():
    while True:
        temperory_int_variable=input('Enter your position : ')
        if not temperory_int_variable.isdigit():
            print('Detected: string, Excpected: int\tEnter again!')
            continue
        elif not int(temperory_int_variable) in range(1,10):
            print('Range Exceeded!(range is from 1 to 9)\tEnter again!')
            continue
        else:
            return int(temperory_int_variable)-1
    
# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# int main()

clear_output()
disco_light()

os.system('pause')

print('\nIndex numbers are as follows')
display_board(list(range(1, 10)))

os.system('pause')

clear_output()

# Calling the input function
details_of_players = player_input()

while True:

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    clear_output()

    while True:

        display_board(board)

        while True:

            # Player 1 Turn

            print(f"{details_of_players['who_plays_first']['name']}'s turn!")
            position = entering_position()
            
            while True:
                if space_check(board, position):
                    place_marker(
                        board, details_of_players['who_plays_first']['marker'], position)
                    break
                else:
                    print('Space already filled!')
                    continue

            clear_output()
            display_board(board)

            if win_check(board, details_of_players['who_plays_first']['marker']):
                print(details_of_players['who_plays_first']['name'], ' wins!')
                break

            if full_board_check(board):
                break

            # Player2's turn.

            print(f"{details_of_players['who_plays_second']['name']}'s turn!")
            position = entering_position()

            while True:

                if space_check(board, position):
                    place_marker(
                        board, details_of_players['who_plays_second']['marker'], position)
                    break
                else:
                    print('Space already filled!')
                    continue

            clear_output()
            display_board(board)

            if win_check(board, details_of_players['who_plays_second']['marker']):
                print(details_of_players['who_plays_second']['name'], ' wins!')
                break

            continue

        break

    if not win_check(board, details_of_players['who_plays_second']['marker']) and not win_check(board, details_of_players['who_plays_first']['marker']):
        print('Match Drawn!\nBetter luck next time!')

    if not replay():
        break
    else:
        continue