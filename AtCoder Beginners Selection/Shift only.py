N = int(input())
A = list(map(int, input().split()))
ans = 0
while all(x % 2 == 0 for x in A):
    A = list(map(lambda i: i // 2, A))
    ans += 1
print(ans)