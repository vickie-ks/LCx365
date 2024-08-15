class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result

solution = Solution()
print(solution.convertToTitle(1))
print(solution.convertToTitle(28))
print(solution.convertToTitle(52))
print(solution.convertToTitle(701))
