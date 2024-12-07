data = open("2024//advent_07.txt", "r")

input = []
for line in data:
    line = line.replace(":","")
    input.append(line.strip("\n").split(" "))

i = 0; k = 0
final_count = 0

while i < len(input):
    # nová iniciace dalšího řádku
    expected_result = int(input[i][0])
    input_numbers = input[i][2:]
    results = [input[i][1]]

    while k < len(input_numbers):
        temp = []
        for result in results:
            temp.append(int(result)+int(input_numbers[k]))
            temp.append(int(result)*int(input_numbers[k]))
            temp.append(int(str(result)+str(input_numbers[k]))) # odstranit pro výsledek části 1

        results = temp
        k+=1
    
    # Vrací výsledek
    if expected_result in results: final_count += expected_result
    
    i += 1; k = 0

print(final_count)