#
# 26. Remove Duplicates from Sorted Array
#
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.removeDuplicates(nums=[1, 1, 2]), 2)

    def test_2(self):
        self.assertEqual(self.s.removeDuplicates(
            nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums[:] = sorted(set(nums))
        # return len(nums)
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[n-1]:
                n += 1
                nums[n-1] = nums[i]
        return n


if __name__ == "__main__":
    unittest.main()
