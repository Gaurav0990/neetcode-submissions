class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_list = []
        for i in strs:
            my_list.append(''.join(sorted(i)))
        
        my_dict = {}
        for j,val in enumerate(my_list):
            if val in my_dict:
                my_dict[val].append(strs[j])
            else:
                my_dict[val] = [strs[j]]

        return(list(my_dict.values()))
