class Solution:
  def canFinish(self, numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for edge in prerequisites:
      graph[edge[0]].append(edge[1])

    visited = set()

    # True if there is a cycle, False if not
    def visit(vertex):
      visited.add(vertex)
      for neighbour in graph[vertex]:
        if neighbour in visited or visit(neighbour):
          return True
      visited.remove(vertex)
      return False

    for i in range(numCourses):
      if visit(i):
        return False
    return True