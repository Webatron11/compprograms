output = "13211311123113112211"
test = list()
chunks = list()
for i in range(len(output)):
    try:
        if output[i] != output[i + 1]:
            test.append(i)
    except IndexError:
        test.append(len(output)-1)

test1 = test[0::2]
test2 = test[1::2]

print([output[test1[i]:test2[i]] for i in range(len(test1))])
