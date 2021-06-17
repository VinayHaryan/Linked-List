class Node:

    def __init__(self, value):
        self.info = value
        self.link = None

class singlelinkedlist:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("list is: ")
            p = self.start
            while p is not None:
                print(p.info, " ", end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("number of nodes in the list= ",n)

    def search(self,x):
        position = 1
        p =self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            position += 1
            p = p.link

        else:
            print(x, "not found in list")
            return False

    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
        

    def insert_in_end(self):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("enter the nuber of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("enter the element to be inserted: "))
            self.insert_in_end(data)

    def insert_after(self):
        pass

    def insert_before(self):
        pass

    def insert_at_position(self):
        pass

    def delete_node(self):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self,x):
        pass

    def merge2(self,list2):
        pass

    def merge3(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def merge_sort_rec(self, listStart):
        pass

    def divide_list(self,p):
        pass



#################################################################3


list = singlelinkedlist()
list.create_list()

while True:
    print("1.display list")
    print("2.count the number of nodes")
    print("3.search for an element")
    print("4.insert in empty list/insert in beginning of the list")
    print("5.insert a node at the end of the list")
    print("6.insert a node at after a specific node")
    print("7.insert a node at before a specific node")
    print("8.insert a node at the given position")
    print("9.delet first node")
    print("10.delet last node")
    print("11.delet any node")
    print("12.reverse the list")
    print("13.bubble sort by exchanging data")
    print("14.bubble sort by exchanging links")
    print("15.merge sort")
    print("16.insert cycle")
    print("17.detect cycle")
    print("18.remove cycle")
    print("19.quit")

    option = int(input("enter your choice: "))

    if option == 1:
        list.display_list()

    elif option == 2:
        list.count_nodes()

    elif option == 3:
        data = int(input("enter the elements to be searched: "))
        list.search(data)

    elif option == 4:
        data = int(input("enter the element to insert"))
        list.insert_in_beginning(data)

    elif option == 5:
        data = int(input("enter the element to insert"))
        list.insert_in_end(data)

    elif option == 6:
        data = int(input("enter the element to insert"))
        x = int(input("enter the element after which to insert: "))
        list.insert_after(data,x)

    elif option == 7:
        data = int(input("enter the element to insert"))
        x = int(input("enter the element before which to insert: "))
        list.insert_before(data,x)

    elif option == 8:
        data = int(input("enter the element to insert"))
        k = int(input("enter the position at which to insert: "))
        list.insert_at_position(data,k)

    elif option == 9:
        list.delete_first_node()

    elif option == 10:
        list.delete_last_node()

    elif option == 11:
        data = int(input("enter the element to be deleted"))
        list.delete_node(data)

    elif option == 12:
        list.reverse_list()

    elif option == 13:
        list.bubble_sort_exdata()

    elif option == 14:
        list.bubble_sort_exlinks()

    elif option == 15:
        list.merge_sort()

    elif option == 16:
        data = int(input("enter the element at which the cycle has to be inserted: "))
        list.insert_cycle(data)

    elif option == 17:
        if list.has_cycle():
            print("list has a cycle")
        else:
            print("list doesnot have a cycle")

    elif option == 18:
        list.remove_cycle()

    elif option == 19:
        break
    
    else:
        print("wrongg option")

    print()

    




    

    

