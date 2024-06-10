# def say_the_sequence(inp):
#     test = [0] + [i for i in range(len(inp)) if inp[i] != inp[i - 1]] + [len(inp)]
#     chunks = [inp[test[i]:test[i + 1]] for i in range(len(test) - 1)]
# 
#     return "".join([str(chunks[i].count(list(set(chunks[i]))[0])) + list(set(chunks[i]))[0] for i in range(len(chunks))])

def say_the_sequence(inp):
    chunks = []
    test = []

    for i in range(len(inp)):
        if inp[i] != inp[i - 1]:
            test.append(i)

    test.append(len(inp))

    for i in range(len(test) - 1):
        try:
            chunks.append(inp[test[i]:test[i + 1]])
        except IndexError:
            pass

    print(chunks)

    for i in range(len(chunks)):
        num = list(set(chunks[i]))[0]
        chunks[i] = str(chunks[i].count(num)) + num

    return "".join([i for i in chunks])


num = int(input("Enter a number: "))
start = "1"

for n in range(num):
    print(start)
    print(say_the_sequence(start))
    start = say_the_sequence(start)
