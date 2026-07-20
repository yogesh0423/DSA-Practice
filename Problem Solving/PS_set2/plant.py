T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n-1):
        ans = max(ans, min(a[i], a[i+1]))
        
    print(ans)


