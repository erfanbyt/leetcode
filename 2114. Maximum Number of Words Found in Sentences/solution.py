# time comlexity: O(n) --> iteration over all the sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_num = 0
        for sentence in sentences:
            len_sentence = len(sentence.split())
            if len_sentence > max_num:
                max_num = len_sentence
            
        return max_num
            
