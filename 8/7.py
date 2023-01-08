from collections import deque

class Node:
    def __init__(self, char): 
        self.go={}
        self.term=False
        self.char=char
        self.suf=None
        self.word=set()
        self.parent=None
        self.visited=False
        self.num=0

class Trie:
    def __init__(self):
        self.root=Node(None)

    def add(self, word,num):
        cur=self.root
        for char in word:
            if char not in cur.go:
                cur.go[char]=Node(char)
                cur.go[char].parent=cur
                cur.go[char].num=num
                num+=1
            cur=cur.go[char]
        cur.term=True
        cur.word.add(word)
        return num

    def build_suf_link(self):
        self.root.suf=None
        q=deque([self.root])
        while q:
            v=q.popleft()
            for c,u in v.go.items():
                t=v.suf
                while t!=None and c not in t.go:
                    t=t.suf
                if t==None:
                    u.suf=self.root
                else:
                    u.suf=t.go[c]
                    if u.suf.term==True:
                        u.term=True
                        u.word.update(u.suf.word)
                q.append(u)

    def automaton(self):
        queue = deque([self.root])
        #self.root.visited=True
        while len(queue) > 0:
            v = queue.popleft()
            for u in v.go:
                if v.go[u].visited == False:
                    v.go[u].visited = True
                    queue.append(v.go[u])
                for char in ['0', '1']:
                    if char not in v.go[u].go:
                        x = v.go[u].suf
                        while x != None and char not in x.go:
                            x = x.suf
                        if x == None:
                            x = self.root
                        if char not in x.go:
                            v.go[u].go[char] = self.root
                        else:
                            v.go[u].go[char] = x.go[char]


    def dfs(self,v):
        used[v.num]=1
        stack.append(v)
        for _,u in v.go.items():
            if used[u.num]==0 and not u.term and self.dfs(u):
                return True
            elif used[u.num]==1 and not u.term:
                return True
            elif used[u.num]==2 and not u.term:
                pass
        used[v.num]=2
        stack.pop()
        return False


trie=Trie()
m=int(input())
word_list=[]
num=0
for i in range(m):
    word=input()
    num=trie.add(word, num)
    word_list.append(word)

stack=[]
used=[False]*(num+1)
trie.build_suf_link()
trie.automaton()
trie.root.num=0
if trie.dfs(trie.root):
    print("NIE")
else:
    print("TAK")


