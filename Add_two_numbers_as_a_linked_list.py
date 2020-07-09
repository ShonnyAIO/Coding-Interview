class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1, l2):
    return self.addTwoNumbersRecursive(l1, l2, 0)
    # return self.addTwoNumbersIterative(l1, l2)

  def addTwoNumbersRecursive(self, l1, l2, c):
    val = l1.val + l2.val + c
    c = val // 10
    ret = Node(val % 10)

    if l1.next != None or l2.next != None:
      if not l1.next:
        l1.next = Node(0)
      if not l2.next:
        l2.next = Node(0)
      ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
    elif c:
      ret.next = Node(c)
    return ret

  def addTwoNumbersIterative(self, l1, l2):
    a = l1
    b = l2
    c = 0
    ret = current = None

    while a or b:
      val = a.val + b.val + c
      c = val // 10
      if not current:
        ret = current = Node(val % 10)
      else:
        current.next = Node(val % 10)
        current = current.next

      if a.next or b.next:
        if not a.next:
          a.next = Node(0)
        if not b.next:
          b.next = Node(0)
      elif c:
        current.next = Node(c)
      a = a.next
      b = b.next
    return ret

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
  print(answer.val, end=' ')
  answer = answer.next
# 7 0 8

# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val):

        self.val = val

        self.next: ListNode = None


class Solution:

    def addTwoNumbers(self, l1, l2, c=0):

        def helper(l1, l2, node, c=0):

            s = l1.val + l2.val + c



            c = s // 10

            s = s % 10



            if not node:

                node = ListNode(s)



            if l1.next and l2.next:

                node.next = helper(l1.next, l2.next, node.next, c)

            elif c > 0:

                l1.next = ListNode(0)

                l2.next = ListNode(0)

                node.next = helper(l1.next, l2.next, node.next, c)



            return node



        return helper(l1, l2, None)



l1 = ListNode(2)

l1.next = ListNode(4)

l1.next.next = ListNode(3)



l2 = ListNode(5)

l2.next = ListNode(6)

l2.next.next = ListNode(4)



result = Solution().addTwoNumbers(l1, l2)

while result:

    print(result.val),

    result = result.next

# 7 0 8
