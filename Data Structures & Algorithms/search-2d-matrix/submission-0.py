class Solution:
    def binary_search(self, num, target):
        left = 0
        right = len(num)-1
        while left <= right:
            mid = (left+right)//2
            if num[mid] == target:
                return True
            elif num[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_list = 0
        right_list = len((matrix))-1
        while left_list <= right_list:
            middle_list = (right_list+left_list)//2
            if self.binary_search(matrix[middle_list], target):
                return True
            elif matrix[middle_list][0] > target:
                right_list = middle_list - 1
            else:
                left_list = middle_list + 1
        return False