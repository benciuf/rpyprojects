import random as rand
import numpy as np
sq_matrix_length = 5

def return_queen_pos(x,y):
    return x,y

def show_board():
    board_matrix = np.zeros((sq_matrix_length, sq_matrix_length))
    print(board_matrix)

def add_queen(x,y):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pos_x = rand.randint(0,sq_matrix_length**2)
    pos_y = rand.randint(0,sq_matrix_length**2)
    print("Board level: ", sq_matrix_length**2)
    print(return_queen_pos(pos_x,pos_y))
    show_board()
    add_queen(pos_x,pos_y)
