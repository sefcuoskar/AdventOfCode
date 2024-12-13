
# with open("2024//advent_09.txt", "r") as file:
#     input = [line.strip('\n') for line in file]

test_input = "2333133121414131402"
input = test_input

# Rozdělení do bloků 
result = []
i = 0; k = 0
while i < len(input):
    a = int(input[i])
    if i % 2 == 1:
        b = "."
    else:   
        b = str(k)
        k += 1

    for j in range(a):
        result.append(b)
    i += 1

i = -1
while "." in result:
    if result[i] == ".":
        result.pop(i)
        i = - 1
        continue

    x = result.index(".")

    result[x] = result[i]
    result.pop(i)




i = 0; checksum = 0
while i < len(result):
    checksum += int(result[i])*i
    i += 1


print("".join(result)) # Kontrolní bod
print(checksum) 
