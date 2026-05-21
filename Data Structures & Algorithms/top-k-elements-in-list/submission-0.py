class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                my_dict = {}

                for i in nums:
                    if i in my_dict:
                        my_dict[i] += 1
                    else:
                        my_dict[i] = 1

                my_dict_sorted = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)[:k]

                return [key for key,_ in my_dict_sorted]
