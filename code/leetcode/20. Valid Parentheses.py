class Solution:
    def isValid(self, text):
        dct = {'(': ')', '{': '}', '[': ']'}
        stack = []
        l = len(text)
        if l == 0:
            return True
        if l % 2 != 0:
            return False
        for num, char in enumerate(text):
            if char in dct:
                stack.append(dct[char])
            elif stack and char == stack[-1]:
                stack.pop(-1)
            else:
                return False
        return not stack