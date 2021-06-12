class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i + 1) for i in range(n)]
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                res[i - 1] = 'Fizz'
            elif i % 5 == 0:
                res[i - 1] = 'Buzz'

        return res
