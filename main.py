import random

sq_matrix_length = 5

def return_queen_pos(x,y):
    return x,y

def show_board():
    for i in range(sq_matrix_length):
        print(" ",i)
        for j in range(sq_matrix_length):
            print(" ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pos_x = random.randint(0,sq_matrix_length**2)
    pos_y = random.randint(0,sq_matrix_length**2)
    print("Board level: ", sq_matrix_length**2)
    print(return_queen_pos(pos_x,pos_y))
