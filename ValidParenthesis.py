class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        for k in s:
            if k in mapping:
                top_value = stack.pop() if stack else '#'
                if mapping[k] != top_value:
                    return False
            else:
                stack.append(k)
        return not stack
s ="()"
output= Solution().isValid(s)
print(output)
        