# run time: O(n^2)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        donot_match = 0

        for word in words:
            for w in word:
                if w not in allowed:
                    donot_match += 1
                    break
            
        return len(words) - donot_match
