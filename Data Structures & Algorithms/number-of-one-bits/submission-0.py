class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        counter =0
        for digit in binary:
            if digit == '1':
                counter +=1
        return counter

        