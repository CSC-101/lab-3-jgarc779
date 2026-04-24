def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # total: 0, 4, 13, 15, 16,    # num: 4, 9, 2, 1
    return total

result = tally([4, 9, 2, 1])