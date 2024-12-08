left = []
right = []

with open('inputs/day1.txt', 'r') as d1:
    for line in d1:
        [a,b] = line.split('   ')
        left.append(int(a))
        right.append(int(b))


def distance(left,right):
    left.sort()
    right.sort()
    dist = 0
    if len(left) != len(right):
        return 'YOU ARE DUM'
    else:
        for i in range(len(left)):
            dist += abs(left[i] - right[i])
        return dist 

print(distance(left,right))

me=[3,4,2,1,3,3]
you=[4,3,5,3,9,3]

def similarity(left,right):
    left1 = list(set(left))
    sim = 0
    for i in range(len(left1)):
        val = left1[i]
        left_count = left.count(val)
        right_count = right.count(val)
        sim += val*left_count*right_count
    return sim

print(similarity(left,right))