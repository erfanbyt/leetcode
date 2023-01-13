class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # to check it if it possible to reshape the matrix
        N,M = len(mat[0]), len(mat)
        T = r*c
        if N*M != T: return mat

        # flatten = [j for sub in mat for j in sub]
        flatten = []
        for i in mat:
            for j in i:
                flatten.append(j)   


        # final matrix with pre-placed zeros
        res = [[0 for size in range(c)] for size in range(r)]
        
        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = flatten[k]
                k+=1
                # print(elm_num)

        return res
