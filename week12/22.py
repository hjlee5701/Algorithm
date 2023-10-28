class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, stack):
            if len(stack) == 2 * n:
                res.append(stack)
                return
            
            if left < n:
                dfs(left +1, right, stack +"(")
            
            if right < left:
                dfs(left, right +1, stack + ")" )

        res = []
        dfs(0, 0, '')
        return res