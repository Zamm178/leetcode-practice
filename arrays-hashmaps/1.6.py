import pdb


def strCompression(input):
    compressed = ""

    count = 0
    prev = ''
    for c in input:
        if prev == '':
            prev = c
            count += 1
        elif prev == c:
            count += 1
            prev = c
        else:
            compressed += prev + str(count)
            count = 1
            prev = c
    return compressed + prev + str(count)


if __name__ == "__main__":
    print(strCompression("aabcccccaaa"))
    print(strCompression("qwertyuiop"))
