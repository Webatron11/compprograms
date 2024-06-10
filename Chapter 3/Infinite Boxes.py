boxNum = input().split(" ")
ruleNum = int(input())
boxes = list()
for i in range(0, ruleNum):
    boxes.append(input())

if len(set(boxNum)) != len(boxNum):
    for i in boxes:
        if i.split(":") not in boxNum:
            break
