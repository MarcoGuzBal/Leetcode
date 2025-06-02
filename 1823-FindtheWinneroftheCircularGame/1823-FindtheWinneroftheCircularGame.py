# Last updated: 6/2/2025, 12:54:50 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque()

        for i in range(1, n + 1):
            queue.append(i)

        print(queue)

        while len(queue) != 1:
            pops = k

            while pops != 0:
                pops -= 1

                if pops == 0:
                    queue.popleft()
                else:
                    popped = queue.popleft()
                    queue.append(popped)

        return queue.popleft()
