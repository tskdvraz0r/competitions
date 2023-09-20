def numIdenticalPairs(nums: List[int]) -> int:
    from itertools import product

    cnt = 0

    for i, j in product(range(len(nums)), range(len(nums))):
        if i == j:
            continue

        elif nums[i] == nums[j]:
            cnt += 1

    return int(cnt / 2)