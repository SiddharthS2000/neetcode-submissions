class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran_map = {
            ']': '[',
            '}': '{',
            ')':'('
        }
        for c in s:
            if stack and c in paran_map:
                if stack[-1] == paran_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False