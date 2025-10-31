from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    Solution().rotate(matrix)

    print("\nRotated Matrix (90° clockwise):")
    for row in matrix:
        print(row)

# Original Matrix:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Rotated Matrix (90° clockwise):
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

