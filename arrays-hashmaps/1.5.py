
def oneAway(input, edit):
    if input == edit:
        return True

    inputChars = {}
    editChars = {}
    oneEdit = 0

    for c in input:
        if c not in inputChars:
            inputChars[c] = 1
        else:
            inputChars[c] += 1

    for c in edit:
        if c not in editChars:
            editChars[c] = 1
        else:
            editChars[c] += 1

    for char, count in inputChars.items():
        if char not in editChars and oneEdit == 0:
            oneEdit += 1
        elif char not in editChars and oneEdit > 0:
            return False
        elif count-1 == editChars[char] or editChars[char] == count+1 and oneEdit == 0:
            editChars[char] -= count
            if editChars[char] <= 0:
                del editChars[char]
            oneEdit += 1
        elif editChars[char] != count:
            return False
        elif editChars[char] == count:
            del editChars[char]

    return len(editChars) == 0 or (len(editChars) == 1 and oneEdit <= 1)


if __name__ == "__main__":
    print(oneAway("pale", "ple") == True)
    print("-----------------")
    print(oneAway("pale", "pAle") == True)
    print("-----------------")
    print(oneAway("ale", "pale") == True)
    print("-----------------")
    print(oneAway("abcda", "abcd") == True)
    print("-----------------")
    print(oneAway("abcdaa", "abcda") == True)
    print("-----------------")
    print(oneAway("abcada", "abcd") == False)
    print("-----------------")
    print(oneAway("qwertyuiop", "qwerty") == False)
