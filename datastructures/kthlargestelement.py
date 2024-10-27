"""
Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element. This means that there could be duplicates.

sorting the array first will produce a 0(nlogn) time complexity.

Can you solve it without sorting?
Yes it is possible using a max heap (aka priority queue) data structure or
a quickselect algorithm

using a max heap will yield a O(n+klogn) time complexity which is better
than 0(nlogn)

On the other hand the best average time complexity case for this problem
is the quickselect algorythm which yields O(n) average time complexity.
However, the worst case for the quick select algorithm is O(n^2)

Also is important to consider that the quick sort algorithm is not stable.
Stability in sorting algorithms means that when two elements have equal keys,
their relative order is preserved in the sorted output.
However, QuickSelect is not a sorting algorithm to begin with,
it's a selection algorithm used to find the kth smallest (or largest)
element in an unsorted array.

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

"""


def kthLargestElement(nums: list[int], k: int) -> int:
    # nums.sort()
    # return nums[len(nums)-k]

    # Kth Largest value kl formula for a sorted array
    kl = len(nums) - k

    # solution using a quickselect algorithm
    # will divide the array into sub arrays
    # recursively until the kth largest element
    # is found
    def quickSelect(l, r):
        # edge case where r is out of range
        if l >= r:
            return
        # select a pivot point usually the last element
        # and create a pointer variable for the 1st element
        pivot, pointer = nums[r], l
        # traverse every element by index in the range of the array
        for i in range(l, r):
            # if the element is <= than the pivot element
            if nums[i] <= pivot:
                # swap the element in the index position being visited
                # for the element at the pointer index position
                nums[i], nums[pointer] = nums[pointer], nums[i]
                # increment the pointer index value by one to visit the next element
                pointer += 1
                # else continue to the next element in the array
        # when all elements have being visited
        # swap the last element in the index position
        # for the element at the pointer index position
        nums[pointer], nums[r] = nums[r], nums[pointer]
        # if the pointer is > than the kl index,
        # return the value of the quicksort of the left sub array
        if pointer > kl: return quickSelect(l, pointer - 1)
        # if the pointer is < than the kl index,
        # return the value of the quicksort of the right sub array
        elif pointer < kl: return quickSelect(pointer + 1, r)
        # otherwise return the element at the pointer index which is the
        # kth largest element in the array
        else: return nums[pointer]

    # return the result of the application of the quickselect algorythm iteratively
    # to the entire array in place
    return quickSelect(0, len(nums)-1)


nums = [3,2,1,5,6,4]
k = 2
print(kthLargestElement(nums, k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kthLargestElement(nums, k))
