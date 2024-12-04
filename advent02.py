data = open("advent02.txt", "r")

temp = []

for line in data:
    line = line.strip("\n")
    temp.append(line.split(" "))

count = 0
i = 0  

while i < len(temp):
    levels = list(map(int, temp[i]))
    k = 0  
    error_rate = 0  
    safe = True 

    while k < len(levels) - 1:
        diff = levels[k] - levels[k + 1]
        if 0 < diff < 4:
            k += 1 
        elif error_rate < 1:
            error_rate += 1
            del levels[k]  
            k = 0  
        else:
            safe = False
            break

    if not safe:
        levels = list(map(int, temp[i]))
        k = 0
        error_rate = 0
        safe = True

        while k < len(levels) - 1:
            diff = levels[k] - levels[k + 1]
            if -4 < diff < 0:
                k += 1  
            elif error_rate < 1:
                error_rate += 1
                del levels[k]  
                k = 0 
            else:
                safe = False
                break

    if safe:
        count += 1  

    i += 1  

print(count)
