n=int(input())
dp=[0]*(n+1)
prev=[0]*(n+1)

for i in range(2,n+1):
    tmp_min=dp[i-1]
    prev[i]=i-1
    if (i%3==0):
        tmp_min=min(dp[i//3], tmp_min)
        if (dp[i//3]<=dp[prev[i]]):
            prev[i]=i//3
    if (i%2==0):
        tmp_min=min(dp[i//2], tmp_min)
        if (dp[i//2]<=dp[prev[i]]):
            prev[i]=i//2      
    dp[i]=tmp_min+1
        

print(dp[n])
j=n
ans=str(n)
if prev[j]==0:
    print (ans)
else:
    while True:
        ans=str(prev[j])+" "+ans
        if prev[j]==1:
            break
        j=prev[j]
    print(ans)