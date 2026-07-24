# Method 1

nums = [5,6,7,7,1,2,3,1,1,1]

hash_map = {}
n = len(nums)

for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    
print(hash_map)


# Method 2

nums = [5,6,7,7,1,2,3,1,1,1]

hash_map = {}

for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1

print(hash_map)
