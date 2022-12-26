# run time: O(n)

class Solution:
    def countPoints(self, rings: str) -> int:

        rod_color = {}
        for i in range(int(len(rings)/2)):

            if rings[2*i+1] in rod_color:
                if rings[2*i] in rod_color[rings[2*i+1]]:
                    continue
                else: 
                    rod_color[rings[2*i+1]] += rings[2*i]

            else:
                rod_color[rings[2*i+1]] = rings[2*i]

        counter = 0
        for value in rod_color.values():
            if len(value) == 3:
                counter += 1

        return counter
