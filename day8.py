antenna_map = []
characters = {'.'}

with open('inputs/day8.txt', 'r') as file:
    for lines in file:
        line = lines[:-1]
        antenna_map.append(lines[:-1])
        character = {a for a in line}
        characters.update(character)

characters.remove('.')
size = len(antenna_map)


def node_creator(antennas,initial_node_map,size):
    node_map = initial_node_map
    for i in range(len(antennas)-1):
        for j in range(i+1,len(antennas)):
            x1 = antennas[i][0]
            y1 = antennas[i][1]
            x2 = antennas[j][0]
            y2 = antennas[j][1]
            dx = x2 - x1
            dy = y2 - y1
            if (0 <= x1-dx < size) and (0 <= y1-dy < size):
                node_map[y1-dy][x1-dx] = 1
            if (0 <= x2+dx < size) and (0 <= y2+dy < size):
                node_map[y2+dy][x2+dx] = 1
    return node_map


def dictionary_of_antennas(antenna_map,characters,size):
    dictionary = {key: [] for key in characters}
    for j in range(size):
        for i in range(size):
            if antenna_map[j][i] in characters:
                dictionary[antenna_map[j][i]].append([i,j])
    return dictionary


xd = [['.' for i in range(12)] for i in range(12)]
xd[3][5] = 'a'
xd[5][6] = 'a'

xd[7][2] = 'b'
xd[6][1] = 'b'

#me = dictionary_of_antennas(xd,{'a','b'},12)
#print(me['a'])

def find_all_nodes(antenna_map,characters,size):
    dictionary = dictionary_of_antennas(antenna_map,characters,size)
    node_map = [[0 for i in range(size)] for i in range(size)]
    for key in characters:
        antennas = dictionary[key]
        node_map = node_creator(antennas,node_map,size)
    return node_map

#nodes = find_all_nodes(antenna_map,characters,size)
#print(sum([sum(a) for a in nodes]))

#DRUGI DEL

def resonance_node_creator(antennas,initial_node_map,size):
    node_map = initial_node_map
    for i in range(len(antennas)-1):
        for j in range(i+1,len(antennas)):
            x1 = antennas[i][0]
            y1 = antennas[i][1]
            x2 = antennas[j][0]
            y2 = antennas[j][1]
            dx = x2 - x1
            dy = y2 - y1
            d = min(abs(dx),abs(dy))
            repeat = max(1,-(-size//d))
            for k in range(repeat):
                if (0 <= x1-k*dx < size) and (0 <= y1-k*dy < size):
                    node_map[y1-k*dy][x1-k*dx] = 1
                if (0 <= x2+k*dx < size) and (0 <= y2+k*dy < size):
                    node_map[y2+k*dy][x2+k*dx] = 1
    return node_map


def find_all_resonance_nodes(antenna_map,characters,size):
    dictionary = dictionary_of_antennas(antenna_map,characters,size)
    node_map = [[0 for i in range(size)] for i in range(size)]
    for key in characters:
        antennas = dictionary[key]
        node_map = resonance_node_creator(antennas,node_map,size)
    return node_map

nodes = find_all_resonance_nodes(antenna_map,characters,size)
print(sum([sum(a) for a in nodes]))