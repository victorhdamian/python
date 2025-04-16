def maxSubArray(nums) -> int:
    n, res = len(nums), nums[0]
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += nums[j]
            res = max(res, cur)
    return res

test_cases = [
   (1, [2,-3,4,-2,2,1,-1,4]),
   (2, [2,-30,10,3,5,6-1,50]),
   (3, [5,4,9,-2,5,23,-30,9]),
   (4, [70,-20,1,-4,6,7,8,2]),
   (5, [56,2,4,8,1,-1,4,-2,])
]

for test in test_cases:
    print(maxSubArray(test[1]))
