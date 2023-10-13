from stack_array import Stack

def is_solvable(the_maze):

    search_locations = Stack()
    search_locations.push(find_start(the_maze))

    while not search_locations.is_empty():
        #row and call index. 
        row, col = search_locations.pop()
        # check left
        # check down
        # check right
        # check up
    return False

def check_coordinate(the_maze,row,col,search_locations):
    # Continuing from here
    pass
def read_maze(filepath):
    fin = open(filepath)
    maze = []
    for lin in fin:
        maze_row = [] #sublist for the bigger one
        #Strip removes the whitespace in the file.
        #be careful in use because there could be extra whitespace. 
        #could use rstrip("\n")
        for c in line.rstrip():
            maze_row.append(c)
        maze.append(maze_row)
    fin.close
    return maze

def print_maze(the_maze):
    #This makes it look a bit prettier. Removes the quotes and what_not
    for maze_row in the_maze:
        #Joins lines with nothing.
        print("".join(maze_row))
        
def find_start(the_maze):
    #public facing software should have something to verify maze. This does not.
    for row_index in range(len(the_maze)): #this goes through rows
        for col_index in range(len(the_maze[row_index])):
        #this goes through colums
            if the_maze[row_index][col_index] == "S":
                return row_index, col_index

if __name__ == "__main__":
    the_maze = read_maze("maze.txt")
    print_maze(the_maze)
    
    print(is_solvable(the_maze))
        
