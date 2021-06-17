'''
DELETE N NODES AFTER M NODES OF A LINKED LIST

given a linked list and two integers M and N.
Traverse the linked list such that retain M nodes
then delete next N nodes, continue the same till
end of the linked list

Examples:

Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9


'''
# python program to delete M nodes after N nodes
# Node class

# class Node:

#     # constructor to initialize the node object
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
    
#     # function to initialize head
#     def __init__(self):
#         self.head = None

#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     # utility function to print the linked LinkedList
#     def printlist(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=' ')
#             temp = temp.next
    
#     def skipMdeleteN(self,M,N):
#         curr = self.head

#         # the main loop that traverses through the
#         # whom list
#         while curr:
#             # skip M nodes
#             for count in range(1,M):
#                 if curr is None:
#                     return 
#                 curr = curr.next

#             if curr is None:
#                 return

#             # start from next node and delete N nodes
#             t = curr.next
#             for count in range(1,N+1):
#                 if t is None:
#                     break
#                 t = t.next

#             # link the previous list with remaining nodes
#             curr.next = t
#             # set current pointer for next iteration
#             curr = t
        
# # driver program to test above function
# # create following linked list
# # 1->2->3->4->5->6->7->8->9->10 
# llist = LinkedList()
# M = 2
# N = 3
# llist.push(10)
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)

# print("M = %d, N = %d\nGiven Linked List is: "%(M,N))
# llist.printlist()
# print()

# llist.skipMdeleteN(M,N)

# print("\nLinked List after deletion is ")
# llist.printlist()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
    
    def skipMdeleteN(self,M,N):
        curr = self.head
        while curr:
            for count in range(1,M):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            t = curr.next
            for count in range(1,N+1):
                if t is None:
                    break
                t = t.next

            curr.next = t
            curr = t

# Driver function

M = 2
N = 3
l = LinkedList()
l.push(10)
l.push(9)
l.push(8)
l.push(7)
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)

l.printlist()
print()
l.skipMdeleteN(M,N)
print()
l.printlist()

            

    

        
        