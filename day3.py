import re

memory = ''

with open('inputs/day3.txt', 'r') as file:
    for line in file:
        memory += str(line)

mul = re.findall(r'mul\((\d+,\d+)\)',memory)

def multiply_memory(list):
    n = len(list)
    sum = 0
    for i in range(n):
        [a,b] = list[i].split(',')
        sum += int(a)*int(b)
    return sum

print(multiply_memory(mul))

def do_memory(memory):
    do = []
    sections = memory.split("do()")
    for i in range(len(sections)):
        section = sections[i].split("don't()")
        do.append(section[0])
    return do

def better_multiply_memory(memory):
    do = do_memory(memory)
    sum = 0
    for i in range(len(do)):
        multiply = re.findall(r'mul\((\d+,\d+)\)',do[i])
        sum += multiply_memory(multiply)
    return sum

print(better_multiply_memory(memory))