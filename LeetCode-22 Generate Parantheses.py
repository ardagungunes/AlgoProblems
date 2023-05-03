class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        result = []

        def recursive(openPara, closedPara):
            if openPara == closedPara == n:
                res.append("".join(stack))
                return

            if openPara < n:
                stack.append("(")
                recursive(openPara + 1, closedPara)
                stack.pop()

            if closedPara < openPara:
                stack.append(")")
                recursive(openPara, closedPara + 1)
                stack.pop()

        recursive(0, 0)
        return result