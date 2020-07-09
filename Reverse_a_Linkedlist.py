# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __str__(self):
    result = str(self.val)
    if self.next:
      result += str(self.next)
    return result

class Solution:
  def reverseList(self, head):
    prev = None
    curr = head
    while (curr != None):
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

print(Solution().reverseList(node))
# 321