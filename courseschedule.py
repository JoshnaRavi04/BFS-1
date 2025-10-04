# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = defaultdict(list)

        for pre in prerequisites:
            indegrees[pre[0]] += 1
            graph[pre[1]].append(pre[0])

        queue = deque()
        count = 0

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                count += 1

        if count == numCourses:
            return True

        if not queue:
            return False

        while queue:
            curr = queue.popleft()
            dependencies = graph[curr]
            if dependencies:
                for dep in dependencies:
                    indegrees[dep] -= 1
                    if indegrees[dep] == 0:
                        queue.append(dep)
                        count += 1

                    if count == numCourses:
                        return True

        return False

