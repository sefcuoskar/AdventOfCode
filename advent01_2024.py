
data = open("advent01.txt","r")

list_1 = []
list_2 = []

for line in data:
    list_1.append(line.split("   ")[0])
    list_2.append(line.split("   ")[1].strip("\n"))

list_1.sort()
list_2.sort()

i = 0
sum = 0

# while i < len(list_1):
#     sum = sum + abs(int(list_1[i]) - int(list_2[i]))
#     i += 1

while i < len(list_1):
    sum = sum + int(list_1[i]) * list_2.count(list_1[i])
    i += 1

print(sum)