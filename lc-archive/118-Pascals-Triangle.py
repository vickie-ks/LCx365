from typing import List

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l, x = [], []
        l.append([1])
        for i in range(1, n):
            k = []
            k.append(1)
            for j in range(0, len(x) - 1):
                k.append(x[j] + x[j + 1])
            k.append(1)
            x = k
            l.append(k)
        return l

s = Solution()
print(s.generate(8))
