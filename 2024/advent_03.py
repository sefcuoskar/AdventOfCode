import re

data = str(open("2024//advent_03.txt", "r").read())

search = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")

result = search.findall(data)

i = 0
count = 0
switch = True

while i < len(result):
    if result[i] == "do()":
        switch = True
        i += 1
        continue
    elif result[i] == "don't()":
        switch = False
    else:
       x = int(str(result[i]).strip("mul(").strip(")").split(",")[0])
       y = int(str(result[i]).strip("mul(").strip(")").split(",")[1])
    
    count = count + x*y*int(switch)

    i += 1

print(count)
