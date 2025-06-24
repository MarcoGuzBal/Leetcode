# Last updated: 6/24/2025, 5:03:55 PM
class Solution:
    def special_merge(self, iinput):
        if len(iinput) == 1: return iinput
        elif len(iinput) == 2:
            if iinput[1][1] < iinput[0][1] :  return iinput
            else: return iinput[::-1]
        else:
            mid = len(iinput)//2
            k1 = self.special_merge(iinput[:mid]);print (k1)
            k2 = self.special_merge(iinput[mid:]);print (k1)

            result = []

            while True:
                if k1[0][1] > k2[0][1] :
                    result.append(k1[0]); k1.pop(0)
                else:
                    result.append(k2[0]); k2.pop(0)

                if not k1: return result + k2
                if not k2: return result + k1


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d1 = {}
        for i in nums:
            d1[i] = d1.get(i,0) + 1
        print (" Unsorted dictionary based on values look like this {}".format(d1))

        rr = self.special_merge([(k,v) for k,v in d1.items()])
        print(" Sorted dictionary based on values look like this {}".format(rr))
        return [t[0] for t in rr[:k]]    
    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:

        d1 = {}
        for i in nums:
            d1[i] = d1.get(i,0) + 1

        d_values = list(d1.values())
        d_keys = list(d1.keys())

        while True:
            status = False
            for j in range(len(d_values)-1):
                if d_values[j] < d_values[j+1]:
                    d_values[j] , d_values[j + 1] =  d_values[j+1], d_values[j]
                    status = True
                    d_keys[j], d_keys[j + 1] = d_keys[j + 1], d_keys[j]
            if status==False: 
                break
        return d_keys[:k]


    def topKFrequent_2(self, nums, k):
        """
        Approach 1: Using Min Heap
        Time Complexity: O(n log k)
        Space Complexity: O(n + k)
        """
        # Count frequencies
        count = Counter(nums)
        
        # Use min heap to keep track of top k elements
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract elements from heap
        return [num for freq, num in heap]        