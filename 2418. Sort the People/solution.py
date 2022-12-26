# run time: O(n)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # dict_ = {}
        # for name, height in zip(names, heights):
        #     dict_[name] = height
        name_height = []
        for name, height in zip(names, heights):
            name_height.append((name, height))

        sorted_items = sorted(name_height, key=lambda item: item[1], reverse=True)

        names = []
        for name,_ in sorted_items:
            names.append(name)

        return names
