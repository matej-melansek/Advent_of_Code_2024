list_of_reports= []

with open('inputs/day2.txt', 'r') as file:
    for line in file:
        report = line.split(' ')
        report[-1] = report[-1].replace('\n','')
        report = list(map(int,report))
        list_of_reports.append(report)

def is_safe(list):
    n = len(list)
    safe = 1
    if list[0]==list[1]:
        safe = 0
    else:
        neg = (list[0]-list[1])/abs(list[0]-list[1])
        for i in range(n-1):
            if list[i]-list[i+1] not in [neg*1, neg*2, neg*3]:
                safe = 0
    return safe

a=[7, 6, 4, 2, 1]
b=[1, 2, 7, 8, 9]
c=[9, 7, 6, 2, 1]
d=[1, 3, 2, 4, 5]
e=[8, 6, 4, 4, 1]
f=[1, 3, 6, 7, 9]

def num_of_safe(list_of_reports):
    num = 0
    for i in range(len(list_of_reports)):
        num += is_safe(list_of_reports[i])
    return num

#print(sum(list(map(is_safe,list_of_reports))))

def dampner(list):
    safe = 0
    for j in range(len(list)):
        list1 = list.copy()
        list1.pop(j)
        if is_safe(list1) == 1:
            safe = 1
    return safe

def is_safe_dampener(list_of_reports):
    n = len(list_of_reports)
    safe = 0
    for i in range(n):
        report = list_of_reports[i]
        if is_safe(report) == 1:
            safe += 1
        else:
            safe += dampner(report)
    return safe

print(is_safe_dampener(list_of_reports))