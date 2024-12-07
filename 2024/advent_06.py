data = open("2024//advent_06.txt", "r")

map = []

for line in data:
    map.append(list(line.strip("\n")))

i = 0
while i < len(map):
    if "^" in map[i]:
        a = int(i)
        c = a
        b = int(map[i].index("^")) 
        d = b
        break
    else:
        i += 1

barrier_count = 0
x,y = 0, 0
while x < len(map):
    while y < len(map[x]):
        if map[x][y] == "." and not (x == a and y == b):
            map[x][y] = "#"

            i = 0
            while i < 100000: 
                # UP
                if map[a][b] =="^":
                    if map[a-1][b] == "#":
                        map[a][b] = ">"
                    else:
                        # map[a][b] = "X"
                        a -= 1
                        map[a][b] = "^"

                # RIGHT
                elif map[a][b] == ">":
                    if map[a][b+1] == "#":
                        map[a][b] = "v"
                    else:
                        # map[a][b] = "X"
                        b += 1
                        map[a][b] = ">"


                # LEFT
                elif map[a][b] =="<":
                    if b-1 < 0 or map[a][b-1] == "#":
                        map[a][b] = "^"
                    else:
                        # map[a][b] = "X"
                        b -= 1
                        map[a][b] = "<"

                # DOWN
                elif map[a][b] =="v":
                    if map[a+1][b] == "#":
                        map[a][b] = "<"
                    else:
                        # map[a][b] = "X"
                        a += 1
                        map[a][b] = "v"
                
                if not 0<=a<len(map) or not  0<=b<len(map[a]):
                    # print("Position not infinite ", x, y)
                    map[x][y] = "."
                    # count = 0
                    # for row in map:
                    #     count += row.count("X")
                    # print("Guard out of bounds after taking ", count, " moves.")
                    # with open("2024//grid.txt", "w") as f:
                    #     for line in map:
                    #         f.write(str(line) +"\n")
                    break
                else:
                    i += 1
            else:
                print("position infinite",x,y)
                barrier_count += 1

        map[c][d] = "^"
        y += 1
    
    y = 0
    x += 1



print(barrier_count)








