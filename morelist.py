import random
matrix = [[random.randint(0,9) for x in range(6)]for y in range(5)]

init_rows = {}


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

def print_matrix(_2dmatrix):
    for i in range(5):
        for j in range(6):
            print _2dmatrix[i][j],'     ',
        print 

def create_initrows(_2dmatrix, map_holder,height,width):
    listup=[]
    listdown=[]
    listright=[]
    listleft=[]
    
    create_rows(listup,(0,0),(0,1),width)
    create_rows(listdown,(height-1,0),(0,1),width)
    create_rows(listleft,(0,0),(1,0),height)
    create_rows(listright,(0,width-1),(1,0),height)
    
    init_rows[UP]=listup
    init_rows[DOWN]=listdown
    init_rows[LEFT]=listleft
    init_rows[RIGHT]=listright
         
 
       
def create_rows(mlist,start_cell,direction,steps):
     for step in range(steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        mlist.append((row, col))

def move(direction,steps):
    offset= OFFSETS[direction]
    init_tiles=init_rows[direction]
    for tiles in range(len(init_tiles)):
        tile=init_tiles[tiles]
        temp_tiles=list()
        row=list()
        create_rows(temp_tiles,tile,offset,steps)
        for val in range(len(temp_tiles)):
            indices=temp_tiles[val]
            row.append(matrix[indices[0]][indices[1]])
        row=merge(row)
        for val in range(len(temp_tiles)):
            indices = temp_tiles[val]
            if row[val] != matrix[indices[0]][indices[1]]:
                matrix[indices[0]][indices[1]]=row[val]
    print_matrix(matrix)
    

print_matrix(matrix)

create_initrows(matrix,init_rows,5,6)

response = -2022

while response != 5:
    response = int(raw_input("Please enter your move: "))
    if response == 1 or response == 2:
        move(response,5)
    elif response ==3 or response == 4:
        move(response,6)
