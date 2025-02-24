# 690. Employee Importance

# Time Complexity: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# BFS Intuition:
# Start from the given employee and traverse the graph level by level.
# Use a queue to keep track of the employees to visit.
# Use a hashmap to store the employee id and the employee object.

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        h = {e.id: e for e in employees}
  
        total = 0
        q = deque([id])
        while q:
            eid = q.popleft()
            total += h[eid].importance
            q.extend(h[eid].subordinates)

        return total
