class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        def is_palindrome(sub_s):
            return sub_s == sub_s[::-1]

        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
            
        return True
        '''
        left = 0 
        right = len(s) - 1
    
        while left < right:
            if s[left] != s[right]:
            
                leftCurr = s[left+1:right+1]
                rightCurr = s[left:right]
            
                return leftCurr == leftCurr[::-1] or rightCurr == rightCurr[::-1]
        
            else:
                left += 1
                right -= 1

        return True