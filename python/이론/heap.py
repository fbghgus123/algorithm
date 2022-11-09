# 힙을 구현할 때 가장 좋은 라이브러리
import heapq
from socket import ALG_SET_AEAD_ASSOCLEN

# heapq.heappush(list, value): 원소 삽입
# heapq.heappop(list): 가장 작은 원소 삭제
# heapq.heapify(heap): 기존 리스트를 힙으로 변환

heap = [5, 3, 6, 1]
heapq.heapify(heap)
heapq.heappush(heap, 4) # 값 대신 튜플 넣으면 맨 앞을 기준으로 힙 정렬

