class Solution:
    def fib(self, first: int, second: int, n: int):
        res = [first, second]
        for i in range(n):
            temp = res[-1] + res[-2]
            res.append(temp)
            with open('output.txt', 'w') as f:
                print(f'\nFibonacci numbers: {res}', file=f)


sol = Solution()
sol.fib(1, 2, 20)

