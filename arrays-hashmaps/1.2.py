def isPermutation(input, perm):
    countsInput = {}
    countsPerm = {}
    for c in input:
        if c not in countsInput:
            countsInput[c] = 1
        else:
            countsInput[c] += 1

    for c in perm:
        if c not in countsPerm:
            countsPerm[c] = 1
        else:
            countsPerm[c] += 1
    return countsInput == countsPerm


if __name__ == "__main__":
    print(isPermutation("abcda", "aacdb"))
    print(isPermutation("aaaaa", "aaaaa"))
    print(isPermutation("abcda", "aacdb"))
    print(isPermutation("qwertyuiop", "qwerty"))
    print(isPermutation("qwertyuiop", "eoiewioeur"))
