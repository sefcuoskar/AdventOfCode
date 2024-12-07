data = open("2024//advent_07.txt", "r")

input = []
for line in data:
    line = line.replace(":","")
    input.append(line.strip("\n").split(" "))

i = 0
final_count = 0

expected_result = int(input[i][0])
input_numbers = input[i][1:]








print("Celkově", final_count)