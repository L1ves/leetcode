#1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Counter for elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Copy non-val elements to the first k positions
                k += 1
        return k

#2)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Counter for elements not equal to val
        while val in nums:
            nums.remove(val)
