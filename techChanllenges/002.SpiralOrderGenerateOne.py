# Generate an N * N 2D array in
# spiral order clock-wise starting from
# the top left corner, using the
# numbers of 1, 2, 3, …, N * N in increasing order.
# Assumptions
# N >= 0
# Examples
# N = 3, the generated matrix is
# { {1,  2,  3}
#   {8,  9,  4},
#   {7,  6,  5} }


class Solution(object):
    def spiralGenerate(self, n):
        """
    input: int n
    return: int[][]
    """
        # write your solution here
        res = []
        for i in range(n):
            res.append([0] * n)

        if n == 0:
            return res

        length = n
        count = 0
        start_v = 1
        while length > 0:
            print(start_v, length, count)
            self.fill_circle(res, start_v, length, count)
            start_v += (length - 1) * 4
            count += 1
            length -= 2
        return res

    def fill_circle(self, res, start_v, len_edge, start_index):
        lt = start_index
        rb = start_index + len_edge - 1

        for i in range(len_edge):
            res[lt][lt + i] = start_v + i

        for i in range(len_edge - 1):
            res[lt + i][rb] = res[lt][rb - 1] + i + 1

        for i in range(len_edge - 1):
            res[rb][rb - i] = res[rb - 1][rb] + i + 1

        for i in range(len_edge - 1):
            res[rb - i][lt] = res[rb][lt + 1] + i + 1

        return res
