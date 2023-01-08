def z_function(string):
    z=[0]*len(string)
    z[0]=len(string)
    L=0
    R=0
    for i in range(1, len(string)):
        k=0
        if i<=R:
            k=min(z[i-L],R-i+1)
        while i+k<len(string) and string[k]==string[i+k]:
            k+=1
        z[i]=k
        if i+z[i]-1>R:
            L=i
            R=i+z[i]-1
    return z

n, n_colors=map(int, input().split())
colors=[_ for _ in input().split()]
string_plus_reverse=colors+colors[::-1]
z=z_function(string_plus_reverse)
ans=[]
for i in range(n,2*n):
    if z[i]%2==0 and z[i]+i==2*n:
        ans.append(n-z[i]//2)
# reverse_plus_string=colors[::-1]+colors
# z_2=z_function(reverse_plus_string)
# for i in range(n, 2*n):
#     if z_2[i]%2==0 and z_2[i]+i==2*n:
#         ans.append(n-z_2[i]//2)
ans.append(n)        
print(*ans)

# 2 2 1 1 2 2 2