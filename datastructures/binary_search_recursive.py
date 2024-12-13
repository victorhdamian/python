def binary_search_recursive(l: int, r: int, nums: list[int], target: int) -> int:
    if l > r:
        return -1
    m = l + (r - l) // 2
    if nums[m] == target:
        return m
    if nums[m] < target:
        return binary_search_recursive(m + 1, r, nums, target)
    return binary_search_recursive(l, m - 1, nums, target)


def search(nums: list[int], target: int) -> int:
    return binary_search_recursive(0, len(nums) - 1, nums, target)


nums = ([-1,0,2,4,6,8])
target = 4
print(search(nums, target))