n = int(input())
nums = list(map(int, input().split()))
nums.sort()

left = 0
right = n-1
minn = 1_000_000_001
answer = []

while left < right:
    summ = nums[left] + nums[right]
    if minn > abs(summ):
        answer = [nums[left], nums[right]]
        minn = abs(summ)
        if summ == 0:
            break
    
    if summ > 0:
        right -= 1
    elif summ < 0:
        left += 1
print(*answer)