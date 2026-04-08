class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[-t for t in count.values()]
        q=deque()
        time=0
        heapq.heapify(maxheap)
        while q or maxheap:
            time+=1
            if not maxheap:
                time=q[0][1]
            else:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time 