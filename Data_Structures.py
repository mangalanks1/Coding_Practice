class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
        
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
# Python program to reverse a linked list 
# Time Complexity : O(n)
# Space Complexity : O(1)
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#New Class 
class LinkedList:
         # Function to initialize head
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning
    def push(self, data):
        newnode= Node(data)
        newnode.next = None
        self.head = newnode

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print temp.data
            temp= temp.next
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def Popback(self):
        curr = self.head
        lifo = curr.data
        self.head = curr.next
        del curr
        return(lifo)
    
    def PeekFront(self):
        current = self.head
        if current==None: 
            print('ERROR: empty Linked List')
        else:
            while(current is not None):
                prev = current
                current = current.next
        return(prev.data)
    
    def PopFront(self):
        current = self.head
        prev =None
        if current==None: print('ERROR: empty Linked List')
        else:
            while(current is not None):

                next = current.next
                #print prev.data
                if next ==None: 
                    prev.next  =None
                    #print"haha"
                    return current.data
                else: 
                    prev = current
                    current = next
    
    def Peek(self):
        return(self.head.data)
