matrix = []

with open('inputs/day4.txt', 'r') as file:
    for line in file:
        letters = [a for a in line]
        matrix.append(letters[:-1])

def up(x,y):
    if y < 3:
        return 0
    elif matrix[x][y-1] == 'M' and matrix[x][y-2] == 'A' and matrix[x][y-3] == 'S':
        return 1
    else:
        return 0

def down(x,y):
    if y > 136:
        return 0
    elif matrix[x][y+1] == 'M' and matrix[x][y+2] == 'A' and matrix[x][y+3] == 'S':
        return 1
    else:
        return 0

def left(x,y):
    if x < 3:
        return 0
    elif matrix[x-1][y] == 'M' and matrix[x-2][y] == 'A' and matrix[x-3][y] == 'S':
        return 1
    else:
        return 0

def right(x,y):
    if x > 136:
        return 0
    elif matrix[x+1][y] == 'M' and matrix[x+2][y] == 'A' and matrix[x+3][y] == 'S':
        return 1
    else:
        return 0
    
def up_left(x,y):
    if x < 3 or y < 3:
        return 0
    elif matrix[x-1][y-1] == 'M' and matrix[x-2][y-2] == 'A' and matrix[x-3][y-3] == 'S':
        return 1
    else:
        return 0

def up_right(x,y):
    if x > 136 or y < 3:
        return 0
    elif matrix[x+1][y-1] == 'M' and matrix[x+2][y-2] == 'A' and matrix[x+3][y-3] == 'S':
        return 1
    else:
        return 0

def down_left(x,y):
    if x < 3 or y > 136:
        return 0
    elif matrix[x-1][y+1] == 'M' and matrix[x-2][y+2] == 'A' and matrix[x-3][y+3] == 'S':
        return 1
    else:
        return 0

def down_right(x,y):
    if x > 136 or y > 136:
        return 0
    elif matrix[x+1][y+1] == 'M' and matrix[x+2][y+2] == 'A' and matrix[x+3][y+3] == 'S':
        return 1
    else:
        return 0
    
def find_xmas(matrix):
    sum = 0
    for i in range(140):
        for j in range(140):
            if matrix[i][j] == 'X':
                sum += up(i,j) + down(i,j) + left(i,j) + right(i,j) + up_left(i,j) + up_right(i,j) + down_left(i,j) + down_right(i,j)
    return sum

def mmss(x,y):
    if matrix[x-1][y-1] == 'M' and matrix[x+1][y-1] == 'M' and matrix[x-1][y+1] == 'S' and matrix[x+1][y+1] == 'S':
        return 1
    else:
        return 0
    
def msms(x,y):
    if matrix[x-1][y-1] == 'M' and matrix[x+1][y-1] == 'S' and matrix[x-1][y+1] == 'M' and matrix[x+1][y+1] == 'S':
        return 1
    else:
        return 0
    
def smsm(x,y):
    if matrix[x-1][y-1] == 'S' and matrix[x+1][y-1] == 'M' and matrix[x-1][y+1] == 'S' and matrix[x+1][y+1] == 'M':
        return 1
    else:
        return 0

def ssmm(x,y):
    if matrix[x-1][y-1] == 'S' and matrix[x+1][y-1] == 'S' and matrix[x-1][y+1] == 'M' and matrix[x+1][y+1] == 'M':
        return 1
    else:
        return 0

def find_x_mas(matrix):
    sum = 0
    for i in range(1,139):
        for j in range(1,139):
            if matrix[i][j] == 'A':   
                sum += mmss(i,j) + msms(i,j) + smsm(i,j) + ssmm(i,j)
    return sum

print(find_x_mas(matrix))

#grdo napisano, popravi če se ti bo dalo