def floydWarshall(adj_matrix):
    dp=[[float("inf")]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j]!=-1:
                dp[i][j]=adj_matrix[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j])
    return dp

N=int(input())
adj_matrix=[[int(j) for j in input().split()] for i in range(N)]

dist_matrix=floydWarshall(adj_matrix)
max=-1
eccentricity=[]
for i in range(N):
    max_row=-1
    for j in range(N):
        if dist_matrix[i][j]>max:
            max=dist_matrix[i][j]
        if dist_matrix[i][j]>max_row:
            max_row=dist_matrix[i][j]
    eccentricity.append(max_row)

print(max)
print(min(eccentricity))