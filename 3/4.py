#D. Отрезки
#Даны отрезки на прямой. Какое максимальное количество отрезков можно выбрать так, чтобы никакие два из них не пересекались? Отрезки считаются открытыми.


n=int(input())
s=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    s.append(a)
#print(s)
s.sort(key=lambda x:x[1])
#print(s)

ans=0
left=0
for l, r in s:
    if (l>=left):
        left=r
        ans+=1
print(ans)