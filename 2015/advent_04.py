import hashlib

input = "iwrupvqb"
result = ""
i = 0
while result[0:6] != "000000":
    input = "iwrupvqb" + str(i)
    input = input.encode('UTF-8')
    result = hashlib.md5(input).hexdigest()
    if i % 10000 == 0:
        print(i)

    i += 1


print(i-1, result)