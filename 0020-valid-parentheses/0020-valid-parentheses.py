class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ""

        for i in range(len(s)):

            #push opening brackets to the stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack += s[i]

            if not stack:
                return False
            
            #pop the most recent valid parenthesis
            elif s[i] == ')' and stack[-1] == '(':
                stack = stack[:-1]
            elif s[i] == ']' and stack[-1] == '[':
                stack = stack[:-1]
            elif s[i] == '}' and stack[-1] == '{':
                stack = stack[:-1]

            elif s[i] == ')' and stack[-1] != '(':
                return False
            elif s[i] == ']' and stack[-1] != '[':
                return False
            elif s[i] == '}' and stack[-1] != '{':
                return False
            

        if stack:
            return False
        
        
        
        return True


            

        