data = open("AdventofCode2024//advent04.txt", "r")

frame = []
for line in data:
    line = list(line.strip("\n"))
    frame.append(line)

i = 0
k = 0
count = 0

## Task 01 
while i < len(frame):
    while k < len(frame[i]):
        if frame[i][k] == "X":
            if k < (len(frame[i])-3) and frame[i][k+1] == "M" and frame[i][k+2] == "A" and frame[i][k+3] == "S":
                count += 1 
            
            if k >= 3 and frame[i][k-1] == "M" and frame[i][k-2] == "A" and frame[i][k-3] == "S":
                count += 1
            
            if i >= 3 and frame[i-1][k] == "M" and frame[i-2][k] == "A" and frame[i-3][k] == "S":
                count += 1
            
            if i < (len(frame) - 3) and frame[i+1][k] == "M" and frame[i+2][k] == "A" and frame[i+3][k] == "S":
                count += 1
            
            if k >= 3 and i >= 3 and frame[i-1][k-1] == "M" and frame[i-2][k-2] == "A" and frame[i-3][k-3] == "S":
                count += 1
            
            if k >= 3 and i <= (len(frame) - 3) and frame[i+1][k-1] == "M" and frame[i+2][k-2] == "A" and frame[i+3][k-3] == "S":
                count += 1
            
            if k < (len(frame[i])-3) and i >= 3 and frame[i-1][k+1] == "M" and frame[i-2][k+2] == "A" and frame[i-3][k+3] == "S":
                count += 1
            
            if k < (len(frame[i])-3) and i <= (len(frame) - 3) and frame[i+1][k+1] == "M" and frame[i+2][k+2] == "A" and frame[i+3][k+3] == "S":
                count += 1
        
        k += 1
    k = 0
    i += 1

print("Result task 01:", count)

i = 1
k = 1
count = 0
while i < len(frame)-1:
    while k < len(frame[i])-1:
        if frame[i][k] == "A":
            if frame[i-1][k-1] == "M" and frame[i+1][k-1] == "M" and frame[i-1][k+1] == "S" and frame[i+1][k+1] == "S":
                count += 1
        
            if frame[i-1][k-1] == "S" and frame[i+1][k-1] == "S" and frame[i-1][k+1] == "M" and frame[i+1][k+1] == "M":
                count += 1

            if frame[i-1][k-1] == "M" and frame[i+1][k-1] == "S" and frame[i-1][k+1] == "M" and frame[i+1][k+1] == "S":
                count += 1

            if frame[i-1][k-1] == "S" and frame[i+1][k-1] == "M" and frame[i-1][k+1] == "S" and frame[i+1][k+1] == "M":
                count += 1

        k += 1

    k = 1
    i += 1

print("Result task 02:", count)
