"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def shift_zero(line):
    """
    method to shift zero at the end.
    """
    for index_i in range(0, len(line)):
        if line[index_i] != 0:
            key = line[index_i]
            index_j = index_i-1
            while index_j >= 0 and line[index_j] == 0:
                line[index_j+1] = line[index_j]
                index_j = index_j-1
            line[index_j+1] = key 	

def merge(mylist):
    """
    method to merge similar kind of tile.
    """
    line = list(mylist)
    shift_zero(line)
    for index in range(0, len(line)-1):
        if line[index] != 0 and line[index] == line[index+1]:
            line[index] += line[index+1]
            line[index+1] = 0
            index += 1
    shift_zero(line)
    return line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.empty_list = list()
        self.grid = list()
        self.init_rows = {}
        self.new_tile_val = 0
        self.reset()
        self.create_initrows(self.grid_height,self.grid_width)
      
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [ [0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.create_empty_list(self.grid_height,self.grid_width)
        self.new_tile()
        self.new_tile()
        self.print_matrix()      

    def create_empty_list(self,grid_height,grid_width):
        """
        method to create list of empty tiles in the grid
        """
        self.empty_list = [(row,col) for row in range(grid_height) for col in range(grid_width)]

    def remove_indices(self,row,col):
        """
        method to remove indices from list
        """
        for index in range(0,len(self.empty_list)-1):
            indices = self.empty_list[index]
            if indices[0] == row and indices[1] == col :
                self.empty_list.pop(index)

    def add_indices(self,row,col):
        """
        method to add indices to list
        """
        is_available = False
        for index in range(len(self.empty_list)):
            indices = self.empty_list[index]
            if indices[0] == row and indices[1] == col :
                is_available = True
                break
        if is_available == False :
            self.empty_list.append((row,col))

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def print_matrix(self):
        for i in range(self.grid_height):
            for j in range(self.grid_width):
               print self.grid[i][j],'     ',
            print 

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == 1 or direction == 2:
            steps = self.grid_height
        elif direction == 3 or direction == 4:
            steps = self.grid_width
        offset = OFFSETS[direction]
        isMoved = False
        init_tiles = self.init_rows[direction]
        for tiles in range(len(init_tiles)):
            tile = init_tiles[tiles]
            temp_tiles = list()
            row = list()
            self.create_rows(temp_tiles,tile,offset,steps)
            for val in range(len(temp_tiles)):
                indices = temp_tiles[val]
                row.append(self.grid[indices[0]][indices[1]])
            row = merge(row)
            for val in range(len(temp_tiles)):
                indices = temp_tiles[val]
                if row[val] != self.grid[indices[0]][indices[1]]:
                    self.set_tile(indices[0],indices[1],row[val])
                    isMoved = True
        if isMoved == True:
            self.new_tile()
            isMoved = False
        self.print_matrix()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        self.new_tile_val = 0
        rand_a = random.randint(0,9)
        if rand_a == 0:
            self.new_tile_val = 4
        else:
            self.new_tile_val = 2

        tile_pos = random.randint(0,len(self.empty_list)-1)
        empty_tile = self.empty_list[tile_pos]
        self.set_tile(empty_tile[0],empty_tile[1],self.new_tile_val)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        if value != 0:
            self.update_empty_tile_list(1,row,col)
        elif value == 0:
            self.update_empty_tile_list(0,row,col)
            
    def update_empty_tile_list(self,action,row,col):
        """
        method to update the list using remove or add indices method
        """
        if action == 1:
            self.remove_indices(row,col)
        elif action == 0:
            self.add_indices(row,col)          

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]

    def create_initrows(self,height,width):
        """
        stores the initial rows for all the directions in dictionary
        """
        listup = list()
        listdown = list()
        listright = list()
        listleft = list()
        self.create_rows(listup,(0,0),(0,1),width)
        self.create_rows(listdown,(height-1,0),(0,1),width)
        self.create_rows(listleft,(0,0),(1,0),height)
        self.create_rows(listright,(0,width-1),(1,0),height)
        self.init_rows[UP] = listup
        self.init_rows[DOWN] = listdown
        self.init_rows[LEFT] = listleft
        self.init_rows[RIGHT] = listright
         
    def create_rows(self,mlist,start_cell,direction,steps):
        """
        create rows for storing in dictionary
        """
        for step in range(steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            mlist.append((row, col))

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


game = TwentyFortyEight(4,4)
response = -2022
while response != 5:
    response = int(raw_input("Please enter your move: "))
    if response !=5:
        game.move(response)
