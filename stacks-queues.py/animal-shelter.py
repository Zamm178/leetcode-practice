from collections import deque


class Animal:
    def __init__(self, name, timestamp) -> None:
        self.name = name
        self.timestamp = timestamp

    def get(self):
        return (self.name, self.timestamp)


class AnimalShelter:
    def __init__(self) -> None:
        self.timestamp = 0
        self.queueCat = deque()
        self.queueDog = deque()

    def enqueue(self, type, name):
        if type == "d":
            self.queueDog.append(Animal(name, self.timestamp))
        elif type == "c":
            self.queueCat.append(Animal(name, self.timestamp))
        self.timestamp += 1

    def dequeueAny(self):
        if len(self.queueCat) == 0:
            return self.dequeueDog()
        elif len(self.queueDog) == 0:
            return self.dequeueCat()
        elif self.queueCat[0].timestamp < self.queueDog[0].timestamp:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

    def dequeueCat(self):
        if len(self.queueCat) == 0:
            return "error, not enough cats"
        else:
            return self.queueCat.popleft()

    def dequeueDog(self):
        if len(self.queueDog) == 0:
            return "error, not enough dogs"
        else:
            return self.queueDog.popleft()

    def print(self):
        print("dogs", end=" ")
        for dog in self.queueDog:
            print(str(dog.get()) + ",", end="")
        print("\ncats",  end=" ")
        for cat in self.queueCat:
            print(str(cat.get()) + ",", end="")
        print("\n--------")


if __name__ == "__main__":
    ss = AnimalShelter()
    ss.enqueue("d", "ca")
    ss.enqueue("c", "da")
    ss.enqueue("d", "retpore")
    ss.enqueue("c", "ca")
    ss.enqueue("d", "wrew")
    ss.print()
    ss.dequeueAny()
    ss.print()
    ss.dequeueDog()
    ss.print()
    ss.dequeueCat()
    ss.print()
    ss.dequeueAny()
    ss.print()
    ss.dequeueAny()
    ss.print()
