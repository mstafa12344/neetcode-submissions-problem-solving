class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reversed_s = binary[::-1]
        thenew = int(reversed_s, 2)
        return thenew