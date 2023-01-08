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

colors=[-1]*(n+1)
def dfs(v,c):
    colors[v]=c
    for u in adj[v]:
        if colors[u]==-1:
            dfs(u,(c+1)%2)
        elif colors[u]==c:
            print("NO")
            exit(0)

c=0
for i in range(1,n+1):
    if colors[i]==-1:
        dfs(i,0)
print("YES")


# 6 7
# 1 2
# 1 3
# 2 3
# 3 4
# 4 5
# 4 6
# 5 6