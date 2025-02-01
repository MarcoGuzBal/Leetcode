class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        Set = set(sentence)

        if len(Set) == 26:
            return True
        
        return False