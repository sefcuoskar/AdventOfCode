data = open("2015//advent_03.txt", "r").read()

matrix = [[0 for _ in range(1000)] for _ in range(1000)]
a = 500
b = 500
i = 0

while i < len(data):
    if data[i] == "<":
        b -= 1
        matrix[a][b] += 1
    elif data[i] == ">":
        b += 1
        matrix[a][b] += 1
    elif data[i] == "^":
        a -= 1
        matrix[a][b] += 1
    else:
        a += 1
        matrix[a][b] += 1
    
    i += 2

a = 500
b = 500
i = 1
while i < len(data):
    if data[i] == "<":
        b -= 1
        matrix[a][b] += 1
    elif data[i] == ">":
        b += 1
        matrix[a][b] += 1
    elif data[i] == "^":
        a -= 1
        matrix[a][b] += 1
    else:
        a += 1
        matrix[a][b] += 1
    
    i += 2

c,d = 0,0
count = 0

while c < 1000:
    while d < 1000:
        if matrix[c][d] > 0:
            count += 1
        d +=1
    d=0
    c+=1

print(count)