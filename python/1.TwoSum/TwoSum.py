class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty hash map
        hash_map = {}
        # Iterate through the array of numbers
        for i, num in enumerate(nums):
            # Check if target - num is in the hash map
            if target - num in hash_map:
                # Return the indices of the two numbers that add up to the target
                return [hash_map[target - num], i]
            # Add the number and its index to the hash map
            hash_map[num] = i
        # If we didn't find a pair of numbers that add up to the target, return an empty list
        return []
