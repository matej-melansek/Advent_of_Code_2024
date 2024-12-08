results = []
numbers = []

with open('inputs/day7.txt', 'r') as file:
    for lines in file:
        line = lines.split(': ')
        num = [int(a) for a in line[1][:-1].split(' ')]
        results.append(int(line[0]))
        numbers.append(num)

def drevo(results,numbers):
    indexes = []
    for i in range(len(results)):
        num = numbers[i]
        temp_tree = [num[0]]
        for j in range(1,len(num)):
            b = num[j]
            temp_tree = [a + b for a in temp_tree] + [a * b for a in temp_tree]
        if results[i] in temp_tree:
            indexes.append(i)
    return indexes

me = [190,3267,83,156,7290,161011,192,21037,292]
you = [[10, 19], [81, 40, 27], [17, 5], [15, 6], [6, 8, 6, 15], [16, 10, 13], [17, 8, 14], [9, 7, 18, 13], [11, 6, 16, 20]]

good_results = drevo(results,numbers)
results1 = [results[i] for i in good_results]

print(sum(results1))

def drevo1(results,numbers):
    indexes = []
    for i in range(len(results)):
        num = numbers[i]
        temp_tree = [num[0]]
        for j in range(1,len(num)):
            b = num[j]
            b_len = len(str(b))
            temp_tree = [a + b for a in temp_tree] + [a * b for a in temp_tree] + [a*(10**b_len) + b for a in temp_tree]
        if results[i] in temp_tree:
            indexes.append(i)
    return indexes

gooder_results = drevo1(results,numbers)
results2 = [results[i] for i in gooder_results]

print(sum(results2))

# NAROBE RAZUMEL: (a*b)||(c*d)... NAROBE, ((a*b)||c)*d...PRAV 

#def drevo1(numbers):
#    temp = [numbers[0]]
#    for i in range(1,len(numbers)):
#        b = numbers[i]
#        temp = [a + b for a in temp] + [a * b for a in temp]
#    return [str(c) for c in temp]

#def drevo2(results,numbers):
#    indexes = []
#    for i in range(len(results)):
#        num = numbers[i]
#        result = str(results[i])
#        for j in range(1,len(num)):
#            l_drevo = drevo1(num[:j])
#            r_drevo = drevo1(num[j:])
#            for k in range(1,len(result)):
#                if result[:k] in l_drevo and result[k:] in r_drevo:
#                    indexes.append(i)
#                    break
#            if i in indexes:
#                break
#    return indexes