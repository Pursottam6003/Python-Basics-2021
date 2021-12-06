def maxDamage(n):
    global a
    if n == 0:
        return a[0]&a[1]
    elif n == len(a)-1:
        return a[n]&a[n-1]
    else:
        return max(a[n]&a[n-1], a[n]&a[n+1])

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(maxDamage(a, i))
    print(*ans)