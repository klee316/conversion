def main():
    data = []
    output = []

    old = input("replace ")
    new = input("by ")

    print("")
    print("Input data from iBox, and type \'get suggestion\'")

    while True:
        line = input("")

        if line.lower() == "get suggestion":
            break

        data.append(line)

    print(data)

    for line in data:
        if "target: \t\t" in line:
            suggestion = line.replace("target: \t\t", "suggestion: \t").replace(old, new)
            output.append(line)
            output.append(suggestion)

        else:
            output.append(line)

    for line in output:
        print(line)


main()
