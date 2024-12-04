data = open("2024//advent_02.txt", "r")

temp = [list(map(int, line.strip().split())) for line in data]
count = 0

def is_safe(report):
    diffs = [report[i] - report[i + 1] for i in range(len(report) - 1)]
    return (
        all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)   
    )

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

for report in temp:
    if is_safe(report) or is_safe_with_dampener(report):
        count += 1

print(count)
