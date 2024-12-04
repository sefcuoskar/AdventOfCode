data = open("2015//advent_02.txt", "r")

# length l, width w, and height h)
# 2*l*w + 2*w*h + 2*h*l
result = 0
bow = 0
for line in data:
    # Task 01
    a = int(line.strip("\n").split("x")[0])
    b = int(line.strip("\n").split("x")[1])
    c = int(line.strip("\n").split("x")[2])
    x = a*b
    y = b*c
    z = c*a
    m = min(x,y,z)

    result += 2*x + 2*y + 2*z + m

    # Task 02
    d = [a,b,c]
    d.sort()
    e = 2*int(d[0]) + 2*int(d[1])

    bow += a*b*c + e

print(result, bow)

