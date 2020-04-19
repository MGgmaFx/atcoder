N = int(input())
l = list(map(int, input().split()))
l.append('END')
ans = l.copy()
for i in range(len(l)):
    ans[i] = 0
try:
    for i in range(len(l)):
        ans[l[i] - 1] += 1
except TypeError:
    pass
for i in ans:
    print(i)