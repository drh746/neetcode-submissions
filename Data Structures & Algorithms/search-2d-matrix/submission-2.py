class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows

        while top < bottom:
            mid_row = top + (bottom - top) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                bottom = mid_row

        if top == rows:
            return False

        row = top

        l, r = 0, cols
        while l < r:
            mid = l + (r - l) // 2
            if target > matrix[row][mid] :
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid
            else:
                return True
        return False
        
        