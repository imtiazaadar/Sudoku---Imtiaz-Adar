
# Imtiaz Adar
# Sudoku Solve
# Date : 27/06/2021
# Email : imtiaz-adar@hotmail.com, imtiazadarofficial@gmail.com


                                                #######################
                                                #                     #
                                                #       SUDOKU        #
                                                #                     #
                                                #######################

                ##########################################################################################
                # To solve Sudoku We've to check 3 things                                                #
                # First of all, we've to check if element is 0 or not. Zero means unsolved.              #
                # Then if it is unsolved, next_empty() function will return it's row and column          #
                # Number with True, otherwise no row, column number and boolean value will be passed     #
                # If that element is unsolved, then guessing number from 1 - 9 will be passed into       #
                # the matched() method. Matched method will check if that guessing number is             #
                # common to other elements those are in the rows, columns or blocks.                     #
                # If common, it will return False and element will be set again to 0.                    #
                # Otherwise, element will be replaced by the guessed value                               #
                # Function will be recursively called till next_empty() returns False                    #
                ##########################################################################################


                # Puzzle 

                # Unsolved

                #  0  0  0   0  7  2   0  0  0    
                #  6  0  0   0  3  0   0  0  0    
                #  0  2  7   5  0  9   6  1  0    

                #  1  0  5   0  6  0   4  2  0    
                #  9  0  2   0  1  5   3  0  0    
                #  0  0  0   9  0  0   0  6  1    

                #  4  0  6   1  0  0   8  3  0    
                #  7  0  0   0  8  0   1  9  0    
                #  0  1  8   0  9  6   0  4  5   

                # Solved
                #  5  3  1   6  7  2   9  8  4    
                #  6  4  9   8  3  1   2  5  7    
                #  8  2  7   5  4  9   6  1  3    

                #  1  8  5   7  6  3   4  2  9    
                #  9  6  2   4  1  5   3  7  8    
                #  3  7  4   9  2  8   5  6  1    

                #  4  9  6   1  5  7   8  3  2    
                #  7  5  3   2  8  4   1  9  6    
                #  2  1  8   3  9  6   7  4  5   


# Printing Sudoku Board  
def board():
    print()
    for row in range(9):
        if row == 3 or row == 6:
            print()
        for col in range(9):
            if col == 2 or col == 5:
                print(f' {puzzle[row][col]}', end='  ')
            elif col < 8:
                print(f' {puzzle[row][col]}', end=' ')
            else:
                print(f' {puzzle[row][col]}', end='')
        print()
    print()


# Finding
# if the next one is empty or not
def next_empty(puzzle):
    isEmpty = False
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                isEmpty = True
                r = row
                c = col
                return r, c, isEmpty
    return None, None, isEmpty


# Checking guessed number is unique in row or not
def unique_in_row(puzzle, guess, row):
    for i in range(9):
        if puzzle[row][i] == guess:
            return False
    return True


# Checking guessed number is unique in column or not
def unique_in_col(puzzle, guess, col):
    for i in range(9):
        if puzzle[i][col] == guess:
            return False
    return True


# Checking guessed number is unique in 3x3 block or not
def unique_in_block(puzzle, guess, row, col):
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3
    for i in range(block_row, block_row + 3):
        for j in range(block_col, block_col + 3):
            if puzzle[i][j] == guess:
                return False
    return True

# Checking matched or not 
def matched(puzzle, guess, row, col):
    return (unique_in_row(puzzle, guess, row) and unique_in_col(puzzle, guess, col) and unique_in_block(puzzle, guess, row, col))

# Placing correctly
def solve(puzzle):
    row, col, isEmpty = next_empty(puzzle)
    if isEmpty == False:
        return True
    else:
        for guessnum in range(1, 10):
            if matched(puzzle, guessnum, row, col):
                puzzle[row][col] = guessnum
                if solve(puzzle):
                    return True
                else:
                    puzzle[row][col] = 0
    return False


# Take Input
def take_input():

    for row in range(9):
        column = []
        for col in range(9):
            items = int(input(f'Row - {row+1}, Column - {col+1} : '))
            column.append(items)
        puzzle.append(column)
    print()
    print('Finished Taking Inputs Successfully !\n')


# Main
def main():
    print('\t\t______WELCOME TO SUDOKU______')
    print()
    
    take_input()
    print('Unsolved Board')
    board()
    status = solve(puzzle)
    if status:
        print('Solved Board')
        board()
    else:
        print('No Solutions !')


# Driver
if __name__ == '__main__':
    puzzle = []
    main()

# End
    