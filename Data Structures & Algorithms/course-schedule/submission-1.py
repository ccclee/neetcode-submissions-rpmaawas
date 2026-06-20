class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        inorder =[0]*numCourses
        need = defaultdict(list)
        q = deque()
        took = 0
    

        for course, prere in prerequisites:
            inorder[course]+=1
            need[prere].append(course)
        for i, n in enumerate(inorder):
            if n==0:
                q.append(i)
        while q:
            pre = q.popleft()
            took+=1
            for course in need[pre]:
                inorder[course]-=1
                if inorder[course]==0:
                    q.append(course)
        return took == numCourses
