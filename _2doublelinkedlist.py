class Node(object):

    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class doublelinkedlist(object):

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("list is empty")
            return

        print("list is: ")
        p = self.start
        while p is not None:
            print(p.info, " ", end="")
            p = p.next
        print()

    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.next