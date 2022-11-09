import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while(scoville[0] < K):
        if len(scoville) < 2:
            return -1
        count += 1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        new = f + s*2
        heapq.heappush(scoville, new)
    
    return count