import random

sq_matrix_length = 5

def return_queen_pos(x,y):
    return x,y

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pos_x = random.randint(0,sq_matrix_length**2)
    pos_y = random.randint(0,sq_matrix_length**2)
    print("Board level: ", sq_matrix_length**2)
    print(return_queen_pos(pos_x,pos_y))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
