# HARD - reversing string
print("".join([i for i in reversed("string")]))

# Flatten a multidimensional array ([[1,2], 3] = [1, 2, 3])
array = [[1, 2], 3]

newarray = list()
(newarray.append(i) if type(i) is not list else (newarray.append(x) for x in i) for i in array)
print(newarray)

for i in array:
    if type(i) is list:
        for x in i:
            newarray.append(x)
    else:
        newarray.append(i)

print(newarray)

# Interweave two strings
string1 = "string"
string2 = "weaves"

print("".join([string1[i] + string2[i] for i in range(max(len(string1), len(string2)))]))
