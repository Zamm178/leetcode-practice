import math


class setOfStacks:
    def __init__(self, threshold=10) -> None:
        self.stacks = []
        self.threshold = threshold

    def push(self, value):
        if len(self.stacks) == 0 or len(self.stacks[-1]) >= self.threshold:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return "error"
        if len(self.stacks[-1]) == 0:
            return self.stacks.pop()
        self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            return self.stacks.pop()

    def popAt(self, index):
        stack_num = index // self.threshold
        stack_idx = index % self.threshold
        try:
            del self.stacks[stack_num][stack_idx]
        except:
            print("index out of bounds")

        for i in range(stack_num+1, len(self.stacks)):
            remove = self.stacks[i][0]
            self.stacks[i-1].append(remove)
            del self.stacks[i][0]

        if self.stacks[-1] == []:
            self.stacks.pop()

    def print(self):
        print(self.stacks)


if __name__ == "__main__":
    ss = setOfStacks()
    ss.push(1)
    ss.push(2)
    ss.push(0)
    ss.push(9)
    ss.push(6)
    ss.push(7)
    ss.push(0)
    ss.push(8)
    ss.push(0)
    ss.push(2)
    ss.push(9)
    ss.push(139)
    ss.push(100)
    ss.push(209)
    ss.print()
    ss.popAt(4)
    ss.print()
    ss.popAt(3)
    ss.print()
    ss.popAt(0)
    ss.print()
    ss.popAt(10)
    ss.print()
    ss.pop()
    ss.pop()
    ss.pop()
    ss.pop()
    ss.print()
    ss.pop()
    ss.pop()
    ss.print()
