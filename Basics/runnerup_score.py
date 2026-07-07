n = int(input())
array = map(int, input().split())
    
result = sorted(set(array),reverse = True)
    
print(result[1])
