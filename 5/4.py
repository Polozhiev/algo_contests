import sys
import threading

def main():
    n, m=(int(i) for i in input().split())
    edges=[]
    for i in range(m):
        coord=[int(i) for i in input().split()]
        edges.append(coord)
        
    adj=[[] for _ in range(n+1)]
    adj_rev=[[] for _ in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj_rev[edges[i][1]].append(edges[i][0])

    used=[False]*(n+1)

    def dfs(v, order):
        used[v]=True
        for u in adj[v]:
            if not used[u]:
                dfs(u, order)
        order.append(v)

    order=[]
    for i in range(1,n+1):
        if not used[i]:
            dfs(i, order)

    #print(order)

    def dfs2(v,c):
        used[v]=True
        colors[v]=c
        for u in adj_rev[v]:
            if not used[u]:
                dfs2(u, c)
            else:
                if colors[u]!=c:
                    if c not in cond_graph[colors[u]]:
                        cond_graph[colors[u]].append(c)   

    colors=[0]*(n+1)
    used=[False]*(n+1)
    c=1

    order.reverse()
    cond_graph=[[] for _ in range(n+1)]
    for v in order:
        if not used[v]:
            dfs2(v,c)
            c+=1 

    #print(colors)
    ans=0
    for i in range(n+1):
        ans+=len(cond_graph[i])
    print(ans)

if __name__=="__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()

# 13 21
# 1 2
# 2 1
# 5 6
# 6 7
# 7 5
# 3 4
# 4 3
# 8 9
# 9 8
# 10 11
# 11 12
# 12 13
# 13 10
# 1 3
# 5 4
# 7 8
# 8 11
# 4 11
# 6 8
# 4 10
# 5 4


