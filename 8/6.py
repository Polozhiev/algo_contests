from collections import deque

class Node:
    def __init__(self, char): 
        self.go={}
        self.term=False
        self.char=char
        self.suf=None
        self.word=set()

class Trie:
    def __init__(self):
        self.root=Node(None)

    def add(self, word):
        cur=self.root
        for char in word:
            if char not in cur.go:
                cur.go[char]=Node(char)
            cur=cur.go[char]
        cur.term=True
        cur.word.add(word)

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

def find(trie, text):
    found=set()
    i=0
    cur=trie.root
    while i<len(text):
        if cur.term:
            found.update(cur.word)
        if text[i] in cur.go:
            cur=cur.go[text[i]]
        else:
            t=cur.suf
            while t!=None and text[i] not in t.go:
                t=t.suf
            if t==None:
                cur=trie.root
            else:
                cur=t.go[text[i]]
        i+=1      
    if cur.term:
        found.update(cur.word)     
    return found

trie=Trie()
text=input()
m=int(input())
word_list=[]
for i in range(m):
    word=input()
    trie.add(word)
    word_list.append(word)

trie.build_suf_link()
found=find(trie, text)

for i in range(m):
    if word_list[i] in found:
        print("Yes")
    else:
        print("No")


