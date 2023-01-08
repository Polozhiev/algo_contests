import collections

def build_all_buildings(adj):
    for i in range(k):
        building=x[i]*m+y[i]
        if x[i]!=0:
            adj[building-m].remove(building)
        if y[i]!=0:
            adj[building-1].remove(building)

def delete_one_building(adj, building_vertex):
    if x[k-i]!=0:
        adj[building_vertex-m].append(building_vertex)
    if y[k-i]!=0:
        adj[building_vertex-1].append(building_vertex)

def bfs(adj, used, start=0):
    queue=collections.deque([start])
    used[start]=True
    while queue:
        v=queue.popleft()
        for u in adj[v]:
            if not used[u]:
                used[u]=True
                queue.append(u)
    return(used)

n,m,k=map(int, input().split())
x=[-1]*k
y=[-1]*k
for i in range(k):
    x[i], y[i]=map(int, input().split())
    x[i]-=1
    y[i]-=1

adj=[[] for i in range(n*m)]
for i in range(n*m):
    if (i+1)%m!=0:
        adj[i].append(i+1)
    if i<n*m-m:
        adj[i].append(i+m)

build_all_buildings(adj)

used=[False]*(n*m)
bfs(adj, used)
if used[n*m-1]:
    print(-1)
    quit()

for i in range(1,k+1):
    building_vertex=x[k-i]*m+y[k-i]
    delete_one_building(adj, building_vertex)
    if (x[k-i]!=0 and used[building_vertex-m]) or (y[k-i]!=0 and used[building_vertex-1]):
        bfs(adj, used, building_vertex)
    if used[n*m-1]:
        break
print(k-i+1)