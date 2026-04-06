from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        retOnes = []
        counter = 0

        while counter <= n:
            binary = bin(counter)[2:]  # convert current number to binary string
            onesNum = 0                # reset counter for each number
            
            for digit in binary:
                if digit == '1':      # count 1s
                    onesNum += 1
            
            retOnes.append(onesNum)   # append count to result
            counter += 1               # move to next number
        
        return retOnes