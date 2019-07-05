class Solution(object):

    def removepairs(self, s):
        while len(s) != 0:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                break
        return s

    def isValid(self, s):
        s = Solution().removepairs(s)
        if len(s) == 0:
            flag = True
        elif len(s) == 1:
            flag = False
        elif len(s) == 2:
            flag = False
        else:
            flag = False

        return flag