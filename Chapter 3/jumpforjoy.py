# path = input("Input string: ")
path = "A>B.#."
pos = 0
while True:
    try:
        match path[pos]:
            case "A":
                pos += 1
            case ".":
                pos += 1
            case "#":
                print("Impossible")
                break
            case ">":
                pos += 4
            case "<":
                pos -= 4
            case "B":
                print("Possible")
                break
    except IndexError:
        # pos -= 1
        while True:
            match path[pos]:
                case ".":
                    pos -= 1
                case "#":
                    print("Impossible")
                    break
                case ">":
                    pos += 4
                case "<":
                    pos -= 4
                case "B":
                    print("Possible")
                    break
