N, K = map(int, input().split())
min = N % K
ans = 0
if min < abs(min - K):
    ans = min
else:
    ans = abs(min - K)
print(ans)