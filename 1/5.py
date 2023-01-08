n, k = map(int, input().split())
lengths=[]
for i in range(n):
    lengths.append(int(input()))
left=0
right=10000000
summ=0
while right-left>1:
    mid=(left+right)//2
    for i in range(len(lengths)):
        summ+=lengths[i]//mid
    if summ>=k:
        left=mid
    else:
        right=mid   
    summ=0

for i in range(len(lengths)):
    summ+=lengths[i]//right
if summ>=k:
    print(right)
else:
    print(left)
