from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        # Build dictionary: each key maps to a list of occurrences
        for i in nums:
            if i not in numbers:
                numbers[i] = []
            numbers[i].append(i)

        # Build a list of (element, frequency)
        freq_list = [(key, len(value)) for key, value in numbers.items()]

        # Sort by frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # Extract the top k elements
        result = [key for key, _ in freq_list[:k]]
        return result


