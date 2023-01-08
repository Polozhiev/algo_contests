def dsu_get(x):
    if parent[x]!=x:
        ans=dsu_get(parent[x])
        parent[x]=ans
        return ans
    return x

def dsu_union(x, y):
    x=dsu_get(x)
    y=dsu_get(y)
    if x!=y:
        if size[x]<size[y]:
            x,y=y,x
        parent[y]=x
        size[x]+=size[y]

def dsu_init():
    for i in range(N):
        parent[i]=i
        size[i]=1        

N, M=map(int,input().split())
G=[]
parent=[0]*N
size=[0]*N

for i in range(M):
    v,u,w=map(int, input().split())
    G.append((v-1,u-1,w))

G.sort(key=lambda x: x[2])
#print(G)
dsu_init()
length_mst=0
for i in range(M):
    if dsu_get(G[i][0])!=dsu_get(G[i][1]):
        dsu_union(G[i][0], G[i][1])
        length_mst+=G[i][2]

print(length_mst)