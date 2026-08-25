class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for chr in s:
            if chr in paran_map:
                if stack and stack[-1] == paran_map[chr]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chr)
        return True if not stack else False

