class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = []
        for task, freq in count.items():
            # 把 freq 放進 max heap
            heapq.heappush(heap, (-freq, task))
            pass

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if q and q[0][1] == time:
                # cooldown 結束，放回 heap
                heapq.heappush(heap, q.popleft()[0])
                pass

            if heap:
                # pop 出目前剩最多的 task
                cycle = heapq.heappop(heap)
                # 做掉一次
                # 如果還有剩，放進 q
                if cycle[0]<-1:
                    q.append([(cycle[0]+1, cycle[1]),time+n+1])
                pass


        return time