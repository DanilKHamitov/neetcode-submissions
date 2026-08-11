class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substr = []
        
        def dfs(open_count, close_count):
            # Если использовали все скобки
            if open_count == n and close_count == n:
                res.append("".join(substr))
                return
            
            # Добавляем открывающую скобку (если можно)
            if open_count < n:
                substr.append('(')
                dfs(open_count + 1, close_count)
                substr.pop()
            
            # Добавляем закрывающую скобку (если можно)
            if close_count < open_count:
                substr.append(')')
                dfs(open_count, close_count + 1)
                substr.pop()
        
        dfs(0, 0)
        return res