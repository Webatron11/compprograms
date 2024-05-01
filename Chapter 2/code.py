# 1. Print the first ten multiples of two (2, 4, 8, 16...) separated by spaces

print(' '.join([str(2**i) for i in range(1, 11)]))

# 2. Return an array of the first twenty fibonacci numbers starting with “1, 1” (an array named x with [1, 1] is defined for you)
array = [1, 1]
[array.append(array[i] + array[i-1]) for i in range(1, 21)]
print(array)

# CHALLENGE: Try and complete this question without the use of x, returning the array at the end (This one is very hard and requires the use of a special operator)

# print([1, 1] + [i for i in range(1, 21)])

# 3. Write a function or lambda to return the amount of unique characters in a string of only lowercase letters (“aaaaa” returns 1, “abcde” returns 5, “aabbabbabab” returns 2)
string = 'aaabccccddddeeeee'


def unique(inst): return len(set(inst))


print(unique(string))


# 4. Write a function or lambda to check if a string is a palindrome (“racecar” reversed is “racecar”, which is a palindrome) (make sure to account for strings with odd and even letter counts)
def palindrome(strint): return True if ''.join([i for i in reversed(strint)]) == strint else False


def palindrome2(strint): return True if strint[::-1] == strint else False


print('yes' if palindrome2('cac') else 'no')


# 5. Write a function which swaps the case of a string (“Among Us” = “aMONG uS”, “Cool. String” = “cOOL. sTRING”)
def swapcaser(strint): return strint.swapcase()
