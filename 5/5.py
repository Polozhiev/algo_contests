import sys
import threading

def main():
    n=int(input())
    m=int(input())
    edges=[]
    for i in range(m):
        coord=[int(i) for i in input().split()]
        edges.append(coord) 

    adj=[[] for _ in range(n+1)]
    adj_rev=[[] for _ in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj_rev[edges[i][1]].append(edges[i][0])

    def dfs(v, order):
        used[v]=True
        for u in adj[v]:
            if not used[u]:
                dfs(u, order)
        order.append(v)

    def dfs2(v,c):
        used[v]=True
        colors[v]=c
        delegate[c] = v
        for u in adj_rev[v]:
            if not used[u]:
                if colors[u]==0:
                    dfs2(u, c)

    used=[False]*(n+1)
    order=[]
    for i in range(1,n+1):
        if not used[i]:
            dfs(i, order)

    colors=[0]*(n+1)
    used=[False]*(n+1)
    c=1

    order.reverse()
    delegate=[0]*(n+1)
    for v in order:
        if not used[v]:
            dfs2(v,c)
            c+=1 

    good_place=[True]*c
    good_place[0]=False
    for i in range(1,n+1):
        for v in adj[i]:
            if (colors[i]!=colors[v]):
                good_place[colors[i]]=False

    print(sum(good_place))
    for i in range(1,c):
        if good_place[i]:
            print(delegate[i], end=" ")


if __name__=="__main__":
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()