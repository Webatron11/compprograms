# Make an unlinked copy of a list
# Convert a list of numbers as strings to a list of ints
# Get every odd letter in a string
# Get every even letter in a string
# Replace all instances of the int 3 with the string “three” in an array
# Return “bizz” if x mod 3 equals 0 else return “buzz” (The spelling mistake is intentional)
# Sort an array in the form [[1,2], [2,1]...] based on the second value (not a one-liner)
# Find an item in an array, return -1 if not found (not a one-liner)

test = ['test', 'test2']
test_unlinked = test.copy()

numberasstrings = ['1', '2', '3', '4']
print([int(i) for i in numberasstrings])

string = "string"

for i in range(len(string)):
    if (i % 2) != 0: print(string[i])

for i in range(len(string)):
    if (i % 2) == 0: print(string[i])

array = [3, 3, 2, 2]

for i in range(len(array)):
    if array[i] == 3: array[i] = 'Three'

print(array)

array = [3, 3, 3, 2, 2, 2]

for i in range(len(array)):
    if array[i] % 3 == 0: print('bizz')
    else: print('buzz')

array = list('string')
array.reverse()
print(str(array))

array = [[2, 1], [3, 2], [4, 3], [1, 2]]
array[0:-1][1].sort()
print(array)

