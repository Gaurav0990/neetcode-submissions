class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        # print(s)

        s1 = ''

        for i in s:
            if i.isalnum():
                s1 = s1 + i
        # print(s1)


        s2 = ''

        for j in reversed(s1):
            s2 = s2 + j
        # print(s2)

        if s1 == s2:
            return True
        else:
            return False
