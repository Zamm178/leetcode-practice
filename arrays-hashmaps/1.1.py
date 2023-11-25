def isUnique(input):
    return len(set(input)) == len(input)


if __name__ == "__main__":
    print(isUnique("abcda"))
    print(isUnique("qwertyuiop"))
