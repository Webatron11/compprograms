# Print the first ten multiples of two (2, 4, 8, 16...) separated by spaces
print(" ".join([str(2**i) for i in range(1, 11)]))
