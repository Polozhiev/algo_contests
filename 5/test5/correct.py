import sys
import threading
 
def main():
    with open('/home/roman/edu/Algo/Contests/test5/data.txt') as f:
        n,m = [int (_) for _ in (f.readline().strip('\n')).split()]
        lines = f.readlines()
    edges=[]
    for line in lines:
        a,b=map(int, line.split())
        edges.append([a,b])
 
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
        delegate[c] = v;
        for u in adj_rev[v]:
            if not used[u]:
                if colors[u]==0:
                    dfs2(u, c)
            else:
                if colors[u]!=c and c not in cond_graph[colors[u]]:
                    cond_graph[colors[u]].append(c)   
 
 
    used=[False]*(n+1)
    order=[]
    for i in range(1,n+1):
        if not used[i]:
            dfs(i, order)
 
    colors=[0]*(n+1)
    used=[False]*(n+1)
    c=1
 
    order.reverse()
    cond_graph=[[] for _ in range(n+1)]
    delegate=[0]*(n+1)
    for v in order:
        if not used[v]:
            dfs2(v,c)
            c+=1 
 
    ans_n=0
    ans_lst=[]
    for i in range(1, c):
         if len(cond_graph[i])==0:
            ans_n+=1
            ans_lst.append(delegate[i])
            # j=0
            # while colors[j]!=i:
            #    j+=1
            # ans_lst.append(j)
    return (ans_n)
    for i in range(len(ans_lst)):
        print(ans_lst[i], end=" ")
    #print(" ".join(map(str,ans_lst)))
 
    # good_place=[1]*c
    # for i in range(1,n):
    #     for v in adj[i]:
    #         if (colors[i]!=colors[v]):
    #             good_place[i]=0
    # print(sum(good_place))
 
 
if __name__=="__main__":
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()