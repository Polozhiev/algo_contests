def bellmanFord(adj_matrix, N, start=0):
    dp=[float("-inf")]*N
    dp[start]=0
    for d in range(N-1):
        for v,u,w in adj_matrix:
            if dp[v-1]!=float("-inf"):
                dp[u-1]=max(dp[u-1], dp[v-1]+w)
    cycle=False
    vertex_in_cycle=-1
    for v,u,w in adj_matrix:
        if dp[v-1]!=float("-inf") and dp[v-1]+w>dp[u-1]:
            cycle=True
            vertex_in_cycle=u-1
            break

    return cycle, dp, vertex_in_cycle

def dfs(adj_matrix,v, used):
    used[v] = True
    stack = [v]
    while stack:
        curr_v = stack.pop()
        for v1,u1,_ in adj_matrix:
            if v1-1==curr_v and not used[u1-1]:
                stack.append(u1-1)
                used[u1-1] = True


def main():
    N,M=map(int, input().split())
    adj_matrix=[[int(j) for j in input().split()] for i in range(M)]

    # from data_generator import generate
    # generate()
    # with open('/home/roman/edu/Algo/Contests/6/data.txt') as f:
    #     N,M = [int (_) for _ in (f.readline().strip('\n')).split()]
    #     lines = f.readlines()
    # adj_matrix=[]
    # for line in lines:
    #     a,b, w=map(int, line.split())
    #     adj_matrix.append([a,b, w])


    cycle, dist, vertex_in_cycle=bellmanFord(adj_matrix,N)
    if dist[N - 1] == float("-inf"):
        print(":(")
    elif cycle:
        used=[False]*N
        dfs(adj_matrix,vertex_in_cycle-1, used)
        if used[N-1]:
            print(":)")
        else:
            print(dist[N-1])
    else:
        print(dist[N-1])


if __name__ == '__main__':
    main()