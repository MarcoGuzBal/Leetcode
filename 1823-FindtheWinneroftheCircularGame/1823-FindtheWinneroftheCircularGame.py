# Last updated: 6/6/2025, 1:07:19 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque()

        for i in range(1, n + 1):
            queue.append(i)

        while len(queue) != 1:
            pops = k

            for i in range(k - 1):
                queue.append(queue.popleft())

            queue.popleft()

        return queue.popleft()
