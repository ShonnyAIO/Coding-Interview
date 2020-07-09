class Solution:
  def reconstructQueue(self, people):
    people.sort(key=lambda x: (-x[0], x[1]))  # O(nlogn)
    res = []
    for p in people:  # O(N)
      res.insert(p[1], p)  # O(n)
    return res

  # Time Complexity O(N^2)
  # Space : O(N)

print(Solution().reconstructQueue(
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]