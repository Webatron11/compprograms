# Return an array of the first twenty fibonacci numbers starting with “1, 1” (an array named x with [1, 1] is defined for you)
x = [1, 1]

[x[i] + x[i-1] for i in range(1, 21)]

print(x)
# for i in range(1, 21):
#     x.append(x[i] + x[i-1])
