import sys
import threading
 
def main():
    n, m=(int(i) for i in input().split())
    edges=[]
    for i in range(m):
        coord=[int(i) for i in input().split()]
        edges.append(coord)
 
    adj=[[] for i in range(n+1)]
    for i in range(m):
        if edges[i][1] not in adj[edges[i][0]]:
            adj[edges[i][0]].append(edges[i][1])
 
    stack=[]
    used=[0]*(n+1)
    
    def find_cycle(v):
        used[v]=1
        stack.append(v)
        for u in adj[v]:
            if used[u]==0 and find_cycle(u):
                return True
            elif used[u]==1:
                global cycle_start
                cycle_start=u
                return True
            elif used[u]==2:
                pass
        used[v]=2
        stack.pop()
        return False
 
    for i in range(1,n+1):
        if used[i]==0:
            if (find_cycle(i)==True):
                print("YES")
                i=0
                while stack[i]!=cycle_start:
                    i+=1
                for j in range(i,len(stack)):
                    print(stack[j], end=" ")
                exit(0)
    print("NO")


if __name__=="__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()