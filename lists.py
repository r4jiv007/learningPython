list1 = [ (x,y) for x in range(4) for y in range(6)]
matrix = [[x+y for x in range(4)] for y in range(6)]

matrix1=[matrix[:] for matrix in range(6)]
matrix[5][3]=2220

print matrix

print matrix1
