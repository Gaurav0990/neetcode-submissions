class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        fut_temp = []

        for i,_ in enumerate(temperatures):
            for j,_ in enumerate(temperatures):
                if j > i and temperatures[j] > temperatures[i]:
                    fut_temp.append(j-i)
                    break
            else:
                fut_temp.append(0)    
        return fut_temp