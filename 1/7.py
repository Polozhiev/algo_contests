from collections import deque

n, k = map(int, input().split())
lst = [int(a) for a in input().split()]
deq=deque(lst)
for i in range(k):
    x=deq[0]
    y=deq[-1]
    if x<y:
        deq.popleft()
        deq.append((x+y)%(2**30))
    else:
        deq.pop()
        deq.appendleft((y-x)%(2**30))
for i in range(n):
    print(deq[i], end=" ")

