# time complexity: O(n^2) --> for iteration over each row and the summation on each row

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        sum_accounts_person = []
        for row in accounts:  # iterates over the rows
            sum_accounts_person.append(sum(row))

        return max(sum_accounts_person)
            
