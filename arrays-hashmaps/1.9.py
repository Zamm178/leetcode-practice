def isRotation(input1, input2):
    input1List = list(input1)
    input2List = list(input2)
    pivot = -1
    input1piv = False
    for i in range(len(input1List)):
        if input1List[i] == input2List[0]:
            pivot = i
            input1piv = True
            break
    if not input1piv:
        for i in range(len(input2List)):
            if input1List[i] == input1List[0]:
                pivot = i
                break
    if pivot == -1:
        return False
    if input1piv:
        input1List = input1List[pivot:] + input1List[:pivot]
    else:
        input2List = input2List[pivot:] + input2List[:pivot]
    return input1List == input2List


if __name__ == "__main__":
    print(isRotation("waterbottle", "erbottlewat"))
    print(isRotation("a", "a"))
    print(isRotation("waterbottle", "waterbottle"))
    print(isRotation("qwertyuiop", "qwertypoiu"))
    print(isRotation("qwertyuiop", "qwertyuiopp"))
