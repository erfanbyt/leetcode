# run time: o(n)

lass Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        if len(s) != len(t):
            return False

        for char in t:
            if char in char_dict and char_dict[char] != 0:
                char_dict[char] -= 1
                continue
            elif char in char_dict and char_dict[char] == 0:
                return False
            elif char not in char_dict:
                return False

        return True
