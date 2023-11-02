# https://leetcode.com/problems/running-sum-of-1d-array/
nums = [3, 1, 2, 10, 1]
# дается список, проходим по длинне списка
# начинаем с 0 индекса его записываем сразу потом 
# каждую итерацию прибавляем сумму последнего
# к соседней ячейке на один шаг
new_nums = []
new_nums.append(nums[0])
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
    new_nums.append(nums[i])
print(new_nums)

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         return [sum(nums[:i+1]) for i in range(len(nums))]