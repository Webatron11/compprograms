# 1 Make an unlinked copy of a list
# 2 Convert a list of numbers as strings to a list of ints
# 3 Get every odd letter in a string
# 4 Get every even letter in a string
# 5 Replace all instances of the int 3 with the string “three” in an array
# 6 Return “bizz” if x mod 3 equals 0 else return “buzz” (The spelling mistake is intentional)
# 7 Sort an array in the form [[1,2], [2,1]...] based on the second value (not a one-liner)
# 8 Find an item in an array, return -1 if not found (not a one-liner)

# 1
test = ['test', 'test2']
test_unlinked = test.copy()

# 2
numberasstrings = ['1', '2', '3', '4']
print([int(i) for i in numberasstrings])

string = "string"

# 3
for i in range(len(string)):
    if (i % 2) != 0: print(string[i])

# 4
for i in range(len(string)):
    if (i % 2) == 0: print(string[i])

array = [3, 3, 2, 2]

# 5
for i in range(len(array)):
    if array[i] == 3: array[i] = 'Three'

array = [3, 3, 3, 2, 2, 2]

# 6
for i in range(len(array)):
    if array[i] % 3 == 0: print('bizz')
    else: print('buzz')

# HARD - reversing string
array = list('string')
array.reverse()
print(str(array))

# 7
array = [[2, 1], [3, 2], [4, 3], [1, 2]]
array[0:-1][1].sort()
print(array)

