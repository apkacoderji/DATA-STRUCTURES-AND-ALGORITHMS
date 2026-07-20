class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            
            if not stack or s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()

        result = "".join(stack)
        return result