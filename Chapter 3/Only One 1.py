num_of_additions = 0
result = input("")
result = int(result)

while True:
    if result - int("1" * len(str(result))) < 0:
        result -= int("1" * (len(str(result))-1))
    else:
        result -= int("1" * len(str(result)))
    if result == 0:
        break
    num_of_additions += 1

print(num_of_additions)
