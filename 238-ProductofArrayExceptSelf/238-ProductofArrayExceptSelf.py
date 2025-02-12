class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left = []
        right = [0] * len(nums)
        leftProd = 1
        rightProd = 1
        
        for i in range(len(nums)):
            print(leftProd)
            left.append(leftProd)
            leftProd = leftProd * nums[i]
        for j in range(len(nums)-1, -1, -1):
            right[j] = rightProd
            rightProd = rightProd * nums[j]

        for k in range(len(nums)):
            answer.append(left[k] * right[k])

        return answer

