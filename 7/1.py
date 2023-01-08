def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def prim_points(adj, start=0):
    length_mst=0
    mst=[]
    used=[False]*N
    queue=set()
    queue.add((0, start))
    dist_to_mst=[float("inf")]*N
    parent=[False]*N
    parent[0]=-1
    dist_to_mst[start]=0
    while queue:
        out_value, v = min(queue) 
        used[v]=True
        mst.append((parent[v],v))
        length_mst+=out_value
        queue.discard((out_value, v))
        for u in adj[v]:
            if dist_to_mst[u[1]]>u[0] and not used[u[1]]:
                queue.discard((dist_to_mst[u[1]],u[1]))
                dist_to_mst[u[1]]=u[0]
                queue.add(u)
                parent[u[1]]=v
    return mst, length_mst

N=int(input())
points=[tuple(map(int, input().split())) for _ in range(N)]

adj=[[] for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        x1,y1=points[i]
        x2,y2=points[j]
        dist = distance(x1, y1, x2, y2)
        adj[i].append((dist,j))
        adj[j].append((dist,i))







mst, length=prim_points(adj)
print(length)
print(N-1)
for i in range(1,len(mst)):
    for j in mst[i]:
        print(j+1, end=" ")
    print()   


