# B. Авторитеты
#Толик придумал новую технологию программирования. Он хочет уговорить друзей использовать ее. Однако все не так просто.
#  i-й друг согласится использовать технологию Толика, если его авторитет будет не меньше ai (авторитет выражается целым числом).
#  Как только i-й друг начнет ее использовать, к авторитету Толика прибавится число bi (попадаются люди, у которых bi < 0).
#  Помогите Толику наставить на путь истинный как можно больше своих друзей.
import collections
import queue

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

#queue=collections.deque()
#prior_q=collections.deque()
queue=MyDeque()
prior_q=MyDeque()

def priorQpush(a):
    queue.append(a)
    if not prior_q.notEmpty():
        prior_q.append(a)    
    else:
        while prior_q.notEmpty() and a[1]<prior_q.getHead()[1]:
            prior_q.popleft()

        prior_q.append(a)


def priorQpop():
    if queue.getTail()==prior_q.getTail():
            prior_q.popleft()
    queue.popleft()



n, A=map(int, input().split())
cand=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    a.append(i+1)
    cand.append(a)
used=[0]*n
cand_pos=[]
cand_neg=[]
for i in cand:
    if i[1]>=0:
        cand_pos.append(i)
    else:
        cand_neg.append(i)

cand_pos.sort(key=lambda x:x[0])

for i in range(len(cand_pos)):
    if cand_pos[i][0]<=A:
        A+=cand_pos[i][1]
       # used[i]=1 
        used[cand_pos[i][2]-1]=1
    else:
        break

cand_neg.sort(key=lambda x:x[0]+x[1])
cand_neg.reverse()

cand=cand_pos+cand_neg
#print(cand)

for i in range(len(cand_neg)):
    if cand_neg[i][0]<=A:
        A+=cand_neg[i][1]
        #used[len(cand_pos)+i]=1
        used[cand_neg[i][2]-1]=1
        priorQpush(cand_neg[i])
    elif not prior_q.notEmpty() and prior_q[0][1]<cand_neg[i][1] and A-prior_q[0][1]>=cand_neg[i][0]:
        A-=prior_q[0][1]
        used[prior_q[0][2]-1]=0
        #prior_q.popleft()
        priorQpop()
        #used[len(cand_pos)+i]=1
        used[cand_neg[i][2]-1]=1
        A+=cand_neg[i][1]
        priorQpush(cand_neg[i])


result = []
for i in range(len(cand_pos)):
    if(used[cand_pos[i][2] - 1] == 1):
        result.append(str(cand_pos[i][2]))
 
for i in range(len(cand_neg)):
    if(used[cand_neg[i][2] - 1] == 1):
        result.append(str(cand_neg[i][2]))      

print(len(result))
print(" ".join(result))






# 4 19
# 16 -8
# 12 -6
# 6 -1
# 11 -10