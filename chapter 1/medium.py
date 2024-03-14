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
print([int(i) for i in ['1', '2', '3', '4']])

string = "string"

# 3
print(string[::2])

# 4
print(string[1::2])

# 5
array = [3, 2, 3, 2]
print([i if i != 3 else "three" for i in array])

# 6
array = [3, 3, 3, 2, 2, 2]
print(['bizz' if (i % 3) == 0 else "buzz" for i in array])

# 7
array = [[2, 1], [3, 2], [4, 3], [1, 2]]
array.sort(key=lambda x: x[1])
print(array)

# 8
array = ["item1", 'item2', "item3"]

try: print(array.index(''))
except ValueError: print(-1)

# This is morgan's code - i couldnt read it in docs.
print(array.index('item2') if "item2" in array else -1)

