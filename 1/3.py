class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data
class MyDeque:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self, n):
        newnode=Node(n)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            return
        else:
            prev=self.head
            prev.next=newnode
            newnode.next=None
            newnode.prev=prev
            self.head=newnode
        return
    def pop(self):
        if self.head.prev is None:
            self.head=None
            self.tail=None
            return
        else:
            self.head=self.head.prev
            self.head.next=None
            return
    def popleft(self):
        if self.tail.next is None:
            self.head=None
            self.tail=None
            return
        else:
            self.tail=self.tail.next
            self.tail.prev=None
            return

    def getTail(self):
        return (self.tail.data)
    
    def getHead(self):
        return (self.head.data)
    
    def notEmpty(self):
        if self.head is None:
            return False
        else:
            return True

    def print(self):
        node=self.tail
        if node is None:
            print("-1")
            print("\n")
            return
        while node is not None:
            print(node.data)
            node=node.next
        print("\n")

n=int(input())
queue=MyDeque()
help_queue=MyDeque()
for i in range(n):
    str=input().split()
    if str[0]=="+":
        num=int(str[1])
        queue.append(num)
        if not help_queue.notEmpty():
            help_queue.append(num)
        else:
            while help_queue.notEmpty() and num<help_queue.getHead():
                help_queue.popleft()
                
            help_queue.append(num)

    elif str[0]=="-":
        if queue.getTail()==help_queue.getTail():
            help_queue.popleft()
        queue.popleft()

    if help_queue.notEmpty():
        print(help_queue.getTail())
    else:
        print(-1)


    