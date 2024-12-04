data = open("advent02.txt", "r")

temp = []

# Read and parse input
for line in data:
    line = line.strip("\n")
    temp.append(line.split(" "))

count = 0
i = 0  # Index for reports

while i < len(temp):
    levels = list(map(int, temp[i]))  # Convert current report to integers
    k = 0  # Reset index for level comparison
    error_rate = 0  # Reset error rate
    safe = True  # Assume safe unless proven otherwise

    # Check for decreasing order
    while k < len(levels) - 1:
        diff = levels[k] - levels[k + 1]
        if 0 < diff < 4:
            k += 1  # Valid difference, continue checking
        elif error_rate < 1:
            error_rate += 1
            del levels[k]  # Remove problematic level
            k = 0  # Restart the check
        else:
            safe = False
            break

    if not safe:
        # Reset for increasing order check
        levels = list(map(int, temp[i]))
        k = 0
        error_rate = 0
        safe = True

        while k < len(levels) - 1:
            diff = levels[k] - levels[k + 1]
            if -4 < diff < 0:
                k += 1  # Valid difference, continue checking
            elif error_rate < 1:
                error_rate += 1
                del levels[k]  # Remove problematic level
                k = 0  # Restart the check
            else:
                safe = False
                break

    if safe:
        count += 1  # Increment count if safe in either condition

    i += 1  # Move to the next report

print(count)
