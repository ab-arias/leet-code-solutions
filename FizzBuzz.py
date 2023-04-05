class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        strnums = []

        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                strnums.append("FizzBuzz")
            elif num % 3 == 0:
                strnums.append("Fizz")
            elif num % 5 == 0:
                strnums.append("Buzz")
            else:
                strnums.append(str(num))

        return strnums