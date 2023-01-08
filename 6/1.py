N,S,F=map(int, input().split())
adj_matrix=[[int(j) for j in input().split()] for i in range(N)]

d=[float("inf")]*N
d[S-1]=0
used=[False]*N

for i in range(N):
    min_d=float("inf")
    min_node=-1
    for v in range(N):
        if not used[v] and (min_node==-1 or d[v]<min_d):
            min_d=d[v]
            min_node=v
    if min_node==-1: 
        print("-1")
        quit(0)
    for u in range(N):
        if not used[u] and adj_matrix[min_node][u]!=-1:
            d[u]=min(d[u], d[min_node]+adj_matrix[min_node][u])
    used[min_node]=True

if (d[F-1] == float("inf")):
    print("-1")
else:
    print(d[F-1])
        


# 6 1 6
# 0 4 0 -1 -1 -1
# -1 0 -1 -1 3 -1
# -1 -1 0 -1 5 -1
# -1 -1 1 0 -1 -1
# -1 -1 -1 -1 0 9
# -1 -1 -1 -1 -1 0