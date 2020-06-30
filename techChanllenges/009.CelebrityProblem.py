# Given an binary matrix of N * N (the only elements in the matrix are 0s and 1s), each of the indices represents one person.

# matrix[i][j] = 1 if and only if person i knows person j (this is single direction, only if matrix[j][i] = 1 such that person j knows person i).

# Determine if there is one celebrity among all N persons, a celebrity is defined as

# He does not know any other person.
# All the other persons know him.
# Return the celebrity's index if there exist one (there could be at most one celebrity, why?), return -1 otherwise.


class Solution(object):
    def celebrity(self, matrix):
        """
    input: int[][] matrix
    return: int
    """
        # write your solution here
        n = len(matrix)
        c = 0
        for i in range(1, n):
            cToi = matrix[c][i]
            if cToi:
                c = i

        for i in range(n):
            if i != c:
                iToc = matrix[i][c]
                cToi = matrix[c][i]
                if iToc == False or cToi == True:
                    c = -1
                    break
        return c
