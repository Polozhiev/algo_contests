import sys 
import threading 
 
def dsu_get(x, exp, parent,real_exp=0):
    real_exp+=exp[x]
    if parent[x]!=x:
        ans, real_exp=dsu_get(parent[x], exp, parent, real_exp)
        #  parent[x]=ans
        return ans, real_exp
    return x, real_exp

def dsu_add(x, value, exp, parent):
    x,_=dsu_get(x, exp, parent)
    exp[x]+=value

def dsu_union(x, y, size, exp, parent):
    x,_=dsu_get(x, exp, parent)
    y,_=dsu_get(y, exp, parent)
    if x!=y:
        if size[x]<size[y]:
            x,y=y,x
        parent[y]=x
        size[x]+=size[y]
        exp[y]-=exp[x]

def main(): 
    n, m = map(int, input().split())
    parent=[0]*n
    size=[0]*n
    exp=[0]*n
    for i in range(n):
        parent[i]=i
        size[i]=1
 
    for i in range(m):
        request=input().split()
        if request[0]=="add":
            dsu_add(int(request[1])-1, int(request[2]),exp, parent)
        elif request[0]=="join":
            dsu_union(int(request[1])-1, int(request[2])-1, size, exp,parent)
        else:
            print(dsu_get(int(request[1])-1,exp, parent)[1])
 
if __name__ =="__main__": 
    sys.setrecursionlimit(150000) 
    threading.stack_size(100000000) 
    thread = threading.Thread(target=main) 
    thread.start()


# 4 9
# add 2 100
# join 2 1
# add 1 50
# join 1 4
# add 4 70
# get 1
# get 2
# get 3
# get 4