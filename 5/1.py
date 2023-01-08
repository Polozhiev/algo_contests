import sys
import threading

def main():
    n, m=(int(i) for i in input().split())
    edges=[]
    for i in range(m):
        coord=[int(i) for i in input().split()]
        edges.append(coord)
    #print(edges)

    edges.sort()
    adj=[[] for i in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    #print(adj)

    global used
    used=[0]*(n+1)

    def dfs(v,c):
        global used
        used[v]=c
        for u in adj[v]:
            if used[u]==0:
                dfs(u,c)

    c=0
    for i in range(1,n+1):
        if used[i]==0:
            c+=1
            dfs(i,c)

    print(c)
    for i in range(1,n+1):
        print(used[i], end=" ")

if __name__=="__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()

# 9 6
# 2 1
# 1 3
# 5 4
# 6 9
# 9 7
# 8 9


# 10 6
# 2 1
# 1 3
# 5 4
# 6 9
# 9 7
# 8 9
