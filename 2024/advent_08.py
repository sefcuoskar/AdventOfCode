with open("2024//advent_08.txt", "r") as file:
    lines = [line.strip('\n') for line in file]

num_lines = len(lines)
line_length = len(lines[0])
height = 10  # total layers

# Create a 3D cube filled with "."
cube = [[[ '.' for _ in range(line_length)] 
              for _ in range(num_lines)] 
              for _ in range(height)]

# Bottom layer (z=0) from the file lines
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        cube[0][y][x] = char

# Example: Change a position (z=5, y=2, x=3) in the cube
print(cube)


with open("2024//grid.txt", "w") as f:
    for line in cube:
        f.write(str(line) +"\n")
# print(cube)