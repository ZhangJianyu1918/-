import heapq

min_heap = []

heapq.heappush(min_heap,8)
heapq.heappush(min_heap,7)
heapq.heappush(min_heap,2)
heapq.heappush(min_heap,3)
heapq.heappush(min_heap,5)

min_element = heapq.heappop(min_heap)

print(min_element)