class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque(
            i for i in range(numCourses)
            if indegree[i] == 0
        )

        need = numCourses

        while q:
            course = q.popleft()
            need -= 1

            for child in graph[course]:
                indegree[child] -= 1

                if indegree[child] == 0:
                    q.append(child)

        return need == 0