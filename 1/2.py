n, m = map(int, input().split())
n_flats = [int(a) for a in input().split()]
letters=[int(a) for a in input().split()]

bounds=[]
count=0
for i in n_flats:
    bounds.append(count)
    count+=i
bounds.append(count)

def BinarySearchFlat(arr, el):
    left=0
    right=n
    mid=(left+right)//2
    while (left<right and el!=arr[mid]):
        if el<arr[mid]:
            right=mid-1
        elif el>arr[mid]:
            left=mid+1
        mid=(left+right)//2
    if el<=arr[mid]:
        return mid
    else:
        return mid+1

flat=-1
for i in letters:
    dorm=BinarySearchFlat(bounds, i)
    flat=i-bounds[dorm-1]
    print(dorm, flat)

