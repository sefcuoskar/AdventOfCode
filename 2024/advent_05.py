data = open("2024//advent_05.txt", "r")

input = []
checks = []
count = 0

for line in data:
    if "|" in line:
        checks.append(line.strip("\n").split("|"))
    elif "," in line:
        input.append(line.strip("\n").split(","))


i = 0
k = 0
switch = True
while i < len(input):
    while k < len(checks):
        if checks[k][0] in input[i] and checks[k][1] in input[i]:
            if input[i].index(checks[k][0]) < input[i].index(checks[k][1]):
                if switch:
                    switch = True
            else:
                input[i][input[i].index(checks[k][0])],input[i][input[i].index(checks[k][1])] = input[i][input[i].index(checks[k][1])], input[i][input[i].index(checks[k][0])]
                
                switch = False
                k = 0
        k += 1

    if not switch:
        
        count += int(input[i][len(input[i])//2])
                
    switch = True
    k = 0
    i += 1


#a[0], a[4] = a[4], a[0]

print(count)