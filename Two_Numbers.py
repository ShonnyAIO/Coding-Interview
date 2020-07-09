class Solution:
  def twoSum(self, nums, target):
    dict = {}
    for i, num in enumerate(nums):
      if target-num in dict:
        return [dict[target-num], i]
      dict[num] = i
    return "ASDFASDFSAD"