def hasDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i]:
                return True
    return False

def hasDupHash(nums):
    myHash = set()
    for i in nums:
        if i in myHash:
            return True
        else:
            myHash.add(i)
    return False

test_cases = [
   (1, [1,2,4,2,5,7,0]),
   (2, [1,2,9,3,4,5]),
   (3, [89,34,1,1,34,23]),
   (4, [9,83,87,2,5,2,9]),
   (5, [3,8,4,6,2,4,9,6])
]

for test in test_cases:
    print(f"{hasDuplicate(test[1])}, {hasDupHash(test[1])}")


