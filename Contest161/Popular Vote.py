N, M = map(int, input().split())
l = list(map(int, input().split()))
total = sum(l)
limit = total * (1 / (4 * M))
n = sum(x >= limit for x in l)
ans = 'No'
if n >= M:
    ans = 'Yes'
print(ans)