class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
            while True:
                product = 1

                for digit in str(n):
                    d = int(digit)

                    if d == 0:
                        product = 0
                        break

                    product *= d

                if product % t == 0:
                    return n
                n += 1