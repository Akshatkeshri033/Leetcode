# Last updated: 8/20/2025, 5:50:24 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary (jholi) banate hain

        for i, num in enumerate(nums):  # Har element ko index ke saath loop karo
            complement = target - num   # Complement nikalte hain

            if complement in num_map:   # Agar complement jholi mein hai
                return [num_map[complement], i]  # Dono index return kar do

            num_map[num] = i  # Nahi mila toh current number jholi mein daal do

        return []  # (Yeh line kabhi chalegi nahi, safety ke liye hai)
