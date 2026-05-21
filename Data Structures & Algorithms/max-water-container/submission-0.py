class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_list = []

        for i, _ in enumerate(heights):
            for j, _ in enumerate(heights):

                if i != j:
                    area = min(heights[i],heights[j]) * abs(j - i)
                    area_list.append(area)

        return max(area_list)    
