def main():

    data = []

    intro = '''Input data and type 
-    \"to ibox\"            or;
-    \"to omm\"             or;
-    \"get regression\"     or;
-    \"get source\"
'''
    print("")
    print(intro)

    while True:
        line = input("")

        if line.lower() == "to ibox":
            ibox(data)
            break

        elif line.lower() == "to omm":
            omm(data)
            break

        elif line.lower() == "get regression":
            regression(data)
            break

        elif line.lower() == "get source":
            source(data)
            break

        data.append(line)


def ibox(data):
    count = 0
    data_new = []

    print()
    print("=" * 100)
    print("Copy & Paste on iBox: ")
    print()

    for line in data:
        if "string id: \t\t" in line:
            line = line.replace("string id: \t\t", "key id: \t\t")
            data_new += [line]
            count += 1

        if "origin: \t\t" in line:

            line = line.replace("[", "")
            line = line.replace("]: ", "/")
            data_new += [line]

        if "build path:\t\t" in line:
            line = line.replace("build path:\t\t", "")
            buildpath = line

            slash_index = data_new[-1].find("/")

            origin = data_new[-1]
            line = origin[:slash_index] + buildpath + "\n"
            data_new[-1] = line

        if "build paths:" in line:
            index = data.index('build paths:')

            slash_index = data_new[-1].find("/")

            keyid = data_new[-2]
            origin = data_new[-1][:slash_index]

            data_new[-1] = origin + data[index + 1]

            for path in data[index + 2:]:
                if path.startswith("/") == True:
                    count += 1
                    data_new += [keyid]
                    data_new += [origin + path]
                elif path == "":
                    break

    printed_count = 0

    if count != 0:
        for line in data_new:
            print(line)
            printed_count += 1

            if printed_count % 2 == 0:
                print("")

        print("count:", count)
    else:
        print("invalid input")

    print("=" * 100)


def omm(data):
    count = 0

    print()
    print("=" * 100)
    print("Copy & Paste on OMM: ")
    print()

    origin_data = []
    origin_data_cleaned = []
    keyid_data = []

    for line in data:
        if "origin: \t\t" in line:
            line = line.replace("origin: \t\t", "Software Project:or:is:")
            line = line[0:line.find("/")]
            origin_data += [line]

        if "key id: \t\t" in line:
            line = line.replace("key id: \t\t", "String ID:or:is:")
            keyid_data += [line]
            count += 1

    for line in origin_data:
        if line not in origin_data_cleaned:
            origin_data_cleaned += [line]

    if count != 0:
        print("￨".join(origin_data_cleaned))
        print()
        print("￨".join(keyid_data))
        print()
        print("count:", count)
    else:
        print("invalid input")

    print("=" * 100)


def regression(data):

    new_data = []
    output_data = []
    not_dup = 1
    count = 0

    for line in data:

        if "regression: \t" in line:
            line = line.replace("regression: \t", "")
            new_data.append(line)
            count += 1

    try:
        output_data = [new_data[0]]
    except:
        ValueError

    print("=" * 100)

    for line in new_data:
        if line not in output_data:
            not_dup += 1
            output_data.append(line)

    if count != 0:
        for line in output_data:
            print(line)
        print()
        print("count:", not_dup)
        print("duplicate removed:", count - not_dup)

    else:
        print("invalid input")

    print("=" * 100)


def source(data):
    count = 0

    print()
    print("=" * 100)
    print("Copy & Paste on OMM: ")
    print()

    source_data = []

    for line in data:
        if "source: \t\t" in line:
            line = line.replace("source: \t\t", "Source:or:is:")
            source_data += [line]
            count += 1

    if count != 0:
        print("￨".join(source_data))
        print()
        print("count:", count)
    else:
        print("invalid input")

    print("=" * 100)


main()

#written by Kathy