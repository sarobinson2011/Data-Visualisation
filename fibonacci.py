class Solution:

    def fib(self):
        res = [1, 2]
        for i in range(15):
            temp = res[-1] + res[-2]
            res.append(temp)
            with open('output.txt', 'w') as f:
                print(f'\nFibonacci numbers: {res}', file=f)


sol = Solution()
sol.fib()

