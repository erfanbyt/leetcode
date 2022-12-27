# run time: O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        char_dict = {}
        for char in magazine:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        print(char_dict)
        for char in ransomNote:
            if char in char_dict and char_dict[char] != 0:
                char_dict[char] -= 1
                continue
            if char in char_dict and char_dict[char] == 0:
                return False
            if char not in char_dict:
                return False

        return True
