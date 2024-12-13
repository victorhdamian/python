def binary_search_iterative(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        # (l + r) // 2 can lead to overflow in non bound variables languages
        m = l + ((r - l) // 2)

        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


nums = ([-1,0,2,4,6,8])
target = 4
print(binary_search_iterative(nums, target))