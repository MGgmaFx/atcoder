N, M = map(int, input().split())
l = list(map(int, input().split()))
total = sum(l)
if total > N:
    ans = -1
else:
    ans = N - total
print(ans)