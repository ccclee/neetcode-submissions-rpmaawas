class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = [0]* numCourses
        needpre=[[]for _ in range(numCourses)]

        for prerequisite, course in prerequisites:
            needpre[prerequisite].append(course)
            pre[course]+=1
        
        queue = deque()
        count=0
        for course in range(numCourses):
            if pre[course]==0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            count+=1
            for course in needpre[course]:
                pre[course]-=1
                if pre[course]==0:
                    queue.append(course)
        return count == numCourses
        