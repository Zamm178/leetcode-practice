def URLify(input):
    newInput = ""
    for a in input:
        if a == " ":
            newInput += "%20"
        else:
            newInput += a
    return newInput


if __name__ == "__main__":
    print(URLify("abc da far"))
    print(URLify("qwerty uiop "))
