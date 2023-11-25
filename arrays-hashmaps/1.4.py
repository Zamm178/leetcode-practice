def palindromePermutation(input):
    counts = {}
    oneOdd = False
    input = input.lower()
    for c in input:
        if not c.isalnum():
            continue
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    print(counts)
    for count in counts.values():
        if count % 2 != 0 and not oneOdd:
            oneOdd = True
        elif count % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    print(palindromePermutation("Tact Coa"))
    print(palindromePermutation("arecrac"))
    print(palindromePermutation("arecrar"))
    print(palindromePermutation("whattahw"))
    print(palindromePermutation("a"))
    print(palindromePermutation("qwertyuiop"))
