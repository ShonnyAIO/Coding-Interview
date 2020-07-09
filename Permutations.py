class Solution:
  def permute(self, nums):
    res = []

    def permuteHelper(start):
      if start == len(nums) - 1:
        res.append(nums[:])
      for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        permuteHelper(start + 1)
        nums[start], nums[i] = nums[i], nums[start]
    permuteHelper(0)
    return res

print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]