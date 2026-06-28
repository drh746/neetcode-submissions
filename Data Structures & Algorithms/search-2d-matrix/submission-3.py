class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])
        l, r = 0, rows * col
        while l < r:
            mid = l + (r - l) // 2
            if target > matrix[mid // col][mid % col]:
                l = mid + 1
            elif target < matrix[mid // col][mid % col]:
                r = mid
            else:
                return True
        return False