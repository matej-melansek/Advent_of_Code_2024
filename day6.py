map_of_guard =[]

with open('inputs/day6.txt', 'r') as file:
    for lines in file:
        line = lines[:-1]
        map_of_guard.append([element for element in line])

directions = [[0,-1],[1,0],[0,1],[-1,0]]

def walk(inital_map_of_guard,initial_location,initial_direction_index,size):
    map_of_guard = inital_map_of_guard
    x = initial_location[0]
    y = initial_location[1]
    direction_index = initial_direction_index
    direction = directions[initial_direction_index]
    while True:
        map_of_guard[y][x] = 'X'
        if not(x+direction[0] in range(size)) or not(y+direction[1] in range(size)):
            return map_of_guard
        elif map_of_guard[y+direction[1]][x+direction[0]] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
            x += direction[0]
            y += direction[1]
        else:
            x += direction[0]
            y += direction[1]

def find_guard(map_of_guard):
    for j in range(130):
        line = map_of_guard[j]
        for i in range(130):
            if line[i] in ['^','>','v','<']:
                return [[i,j],['^','>','v','<'].index(map_of_guard[j][i])]

guard = find_guard(map_of_guard)

skkkkkk = [['.','.','.','.','#','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','#'],['.','.','.','.','.','.','.','.','.','.'],['.','.','#','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','#','.','.'],['.','.','.','.','.','.','.','.','.','.'],['.','#','.','.','^','.','.','.','.','.'],['.','.','.','.','.','.','.','.','#','.'],['#','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','#','.','.','.']]

guard_walk = walk(map_of_guard,guard[0],guard[1],130)

def len_guard_walk(guard_walk):
    sum = 0
    for j in range(len(guard_walk)):
        line = guard_walk[j]
        for i in range(len(line)):
            if line[i] == 'X':
                sum += 1
    return sum

#print(len_guard_walk(guard_walk))

def add_obstacles(map_of_guard1):
    sum = 0
    for j in range(len(map_of_guard1)):
        for i in range(len(map_of_guard1[j])):
            if map_of_guard1[j][i] == '.':
                temp = [line[:] for line in map_of_guard1]
                temp[j][i] = '#'
                #if walk(temp,guard[0],guard[1],130) == True:
                if walk(temp,[4,6],0,10) == True:
                    sum += 1
    return sum


#### CHEATING AMPAK SEM MEL ISTO IDEJO

sr = guard[0][1]
sc = guard[0][0]
p1 = 0
p2 = 0


for o_r in range(130):
    for o_c in range(130):
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        SEEN = set()
        SEEN_RC = set()
        while True:
            if (r,c,d) in SEEN:
                p2 += 1
                break
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<130 and 0<=cc<130):
                if map_of_guard[o_r][o_c]=='#':
                    p1 = len(SEEN_RC)
                break
            if map_of_guard[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc

print(p2)