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


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(6)
    ll.insert(0)
    ll.insert(5)
    ll.printLL()
    ll.delete(3)
    ll.delete(1)
    ll.delete(5)
    ll.printLL()
