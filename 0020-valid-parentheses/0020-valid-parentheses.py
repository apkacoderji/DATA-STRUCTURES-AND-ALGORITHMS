class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # will hold unmatched opening brackets, in order seen

        for i in range(len(s)):

            # push opening brackets onto the stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            # guard: if we're looking at a closing bracket and the stack
            # is empty, there's nothing for it to match -> invalid.
            # this also prevents a crash on stack[-1] a few lines below,
            # since you can't peek the top of an empty stack.
            if not stack:
                return False

            # pop the most recent valid parenthesis (top of stack matches
            # the current closing bracket)
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()

            # current char is a closing bracket, but the top of the stack
            # does NOT match it -> mismatched brackets, invalid
            elif s[i] == ')' and stack[-1] != '(':
                return False
            elif s[i] == ']' and stack[-1] != '[':
                return False
            elif s[i] == '}' and stack[-1] != '{':
                return False

        # after processing every character, if anything is left unmatched
        # on the stack (an opening bracket with no closer), it's invalid
        if stack:
            return False

        return True