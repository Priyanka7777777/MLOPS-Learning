def stats(nums):
    mx = max(nums)
    mn = min(nums)
    avg = sum(nums) / len(nums)
    return mx, mn, avg
print(stats([1, 2, 3, 4, 5]))