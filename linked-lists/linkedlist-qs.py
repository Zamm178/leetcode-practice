import pdb
# base on linked list structure


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data) -> None:
        node = Node(data)
        curr = self.head
        # if exists
        if self.head:
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def delete(self, data) -> None:
        prev = None
        curr = self.head
        while curr.data != data:
            prev = curr
            curr = curr.next
        # delete here
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next

        # 2nd way
        # curr = self.head
        # if curr.data == data:
        #     temp = curr
        #     self.head = temp.next
        #     return
        # while curr.next:
        #     if curr.next.data == data:
        #         curr.next = curr.next.next
        #         return
        #     curr = curr.next

    def printLL(self) -> None:
        curr = self.head
        if self.head is None:
            print("empty")
            return
        while curr.next:
            print(str(curr.data) + "->", end="")
            curr = curr.next
        print(curr.data)

    def removeDupes(self):
        counts = {}
        curr = self.head
        prev = None
        while curr.next:
            if curr.data not in counts:
                counts[curr.data] = 1
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

    def partition(self, x):
        before = LinkedList()
        after = LinkedList()
        while curr.next:
            if curr.data < x:
                before.insert(self.data)
            else:
                after.insert(self.data)
            curr = curr.next
            before.next = after.head

    def sumLists(self, other):
        curr = self.head
        curr2 = other.head
        carryover = 0
        while curr and curr2:
            sumVal = curr.data + curr2.data + carryover
            if sumVal >= 10:
                curr.data = sumVal % 10
                carryover = sumVal // 10
            else:
                curr.data = sumVal
            curr = curr.next
            curr2 = curr2.next

    def reverse(self):
        prev = None
        while self.head:
            temp = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = temp
        self.head = prev

    def reverseK(self, k):
        prev = None
        for i in range(k):
            while self.head:
                temp = self.head.next
                self.head.next = prev
                prev = self.head
                self.head = temp
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll2 = LinkedList()
    ll.insert(7)
    ll.insert(1)
    ll.insert(8)
    ll2.insert(5)
    ll2.insert(9)
    ll2.insert(2)
    ll.printLL()
    ll.sumLists(ll2)
    ll.printLL()
    ll.reverse()
    ll.insert(18)
    ll.insert(3)
    ll.printLL()
    ll.reverseK(2)
    ll.printLL()
