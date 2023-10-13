
# should work with either one!
from stack_linked import Stack
#from stack_array import Stack
import copy

def main():
    n = int(input("Enter n: "))
    max_solutions = int(input("Enter max solutions (-1 for inf): "))
    debug = input("Debug mode (y/n): ").lower()=="y"
    # print (debug)
    solve_nqueens(n,max_solutions,debug)

def solve_nqueens(n,max_solutions=-1,debug=False):

    found_solutions = Stack()
    board_stack = Stack()
    my_board = BoardState(n)
    #my_board.display()
    board_stack.push(my_board.clone())
    while len(board_stack) > 0 and (len(found_solutions) < max_solutions or max_solutions == -1):        
        temp_board = board_stack.pop()
        #temp_board.display()
        #temp_board.is_solved()
        if debug:
            #print(f'current board state')
            temp_board.display()
            input('Press enter to continue')
        if temp_board.is_solved():
            #print(f'SOLUTION {len(found_solutions)+1} FOUND:')
            temp_board.display(True)
            #print('I\'m solved')
            found_solutions.push(temp_board)
        else:
            
            ######temp_stack = my_board.explore_state()
            temp_stack = temp_board.explore_state()
            #print(f'temp_stack {len(temp_stack)}')
            while len(temp_stack) > 0:
                board_stack.push(temp_stack.pop())
                #print('another round')
            #print(f'board_stack {len(board_stack)}')
            #print(f'Number of Boards Created to be Destroyed Later: {temp_board.number_of_boards}')
    print(f'Number of Boards Created to Only be Destroyed: {temp_board.number_of_boards}')
    print(f'---{len(found_solutions)} solutions found---')
    while len(found_solutions) > 0:
        print(f'SOLUTION {len(found_solutions)}:')
        found_solutions.pop().display(True)
            
    
class BoardState:
    #board = [] Dammit python stop sharing across all instances
    number_of_boards = [0]
    
    def __init__(self,n):
        #print(f'length of new array = {n}')
        self.board = []
        for i in range(n):
            sublist = []
            for j in range(n):
                #if i == j:
                #    sublist.append('Q') 
                #else:
                    sublist.append('_')
                    #print(f'On element: {i} | {j}')
            self.board.append([])
            self.board[i] = sublist
        
        self.number_of_boards[0] += 1
        self.generation = 0
            
    
    def display(self,queens_only=False):
        #print('-----------Board State-------------')
        #print(f'-----------Generation {self.generation}--------------')
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
               
                if queens_only:
                    if self.board[i][j].upper() == "Q":
                        print("Q", end = ' ')
                    else:
                        print('_', end = ' ')
                else:
                     print(self.board[i][j], end = " ")
            #print(f'Length of sublist: {len(self.board[i])}')
            print('') #extra new line
        print('') #extra new line
        #print('-----------------------------------')


    def clone(self):
        n = len(self.board)
        #print(f'old board length: {len(self.board)}')
        new_board = BoardState(n)

        #print(f'new board length: {len(new_board.board)}')
        #new_board.display()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                new_board.board[i][j] = self.board[i][j]
                new_board.generation = self.generation + 1
                #print(f'copying data at {i} | {j}')
        return new_board

    
    def is_solved(self):

        number_of_queens = 0
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].upper() == "Q":
                    number_of_queens += 1
        #print (number_of_queens == len(self.board))
        return number_of_queens == len(self.board)
      

    def explore_state(self):

        new_stack = Stack()
        queen_in_rows = None
        for i in range(len(self.board)):
            
            for j in range(len(self.board[i])):
                if self.board[i][j].upper() == "Q":
                    queen_in_rows = i
            if queen_in_rows is not None and i == queen_in_rows + 1:
            # scan for '_'
                for k in range(len(self.board[i])):
                    if self.board[i][k] == '_':
                        #print(f'adding board to explore {i} | {k}')
                        temp_board = self.clone()
                        #temp_board.display()
                        temp_board.place_queen(i, k) 
                        # Add to stack
                        new_stack.push(temp_board)
                        #temp_board.display()

                # copy this board, place new queen in row
            else:
               queen_in_rows = queen_in_rows
        if queen_in_rows is None:
            i=0
            for k in range(len(self.board[i])):
                    if self.board[i][k] == '_':
                        #print(f'adding board to explore {i} | {k}')
                        temp_board = self.clone()
                        temp_board.place_queen(i, k) 
                        new_stack.push(temp_board)
            #print('Q\'s seeded... ...RESTARTING...')
        return new_stack
                                
    
    def place_queen(self,row,col):

        #print('place queen')
        self.board[row][col] = 'Q'
        temp_row = row
        temp_col = col

        #print(temp_row)
        #print(f' length of board {len(self.board)}')
        #print('fill left and down')
        while temp_row < len(self.board)-1 and temp_col > 0:
            temp_col -= 1
            temp_row += 1
            self.board[temp_row][temp_col] = '/'
            #print(f' place at {temp_row} | {temp_col}')
        temp_row = row
        temp_col = col

        
        #print(f' length of board {len(self.board)}')
        #print('fill straight down')
        while temp_row < len(self.board)-1:
            temp_row += 1
            self.board[temp_row][temp_col] = '|'
            #print(f' place at {temp_row} | {temp_col}')
        
        
        temp_row = row
        temp_col = col

        #print('fill right and down')
        while temp_row < len(self.board)-1 and temp_col < len(self.board[row])-1:
            temp_col += 1
            temp_row += 1
            self.board[temp_row][temp_col] = '\\'
            #print(f' place at {temp_row} | {temp_col}')
            
        
        #print('placed queen(s)')
    
if __name__ == "__main__":
    main()
