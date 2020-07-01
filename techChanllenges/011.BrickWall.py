# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# H * W, total edges is P, and total bricks is N

# Time Limit Exceeded - too slow - O(H*P)
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = len(wall)
        edge = 0
        bricks = [l.pop() for l in wall]

        def fill(bricks, wall):
            for i in range(len(bricks)):
                if bricks[i] == 0:
                    if len(wall[i]) == 0:
                        return True
                    else:
                        bricks[i] = wall[i].pop()

            return False

        def cut(bricks):
            short = min(bricks)
            count = 0
            for i in range(len(bricks)):
                bricks[i] -= short
                if bricks[i] == 0:
                    count += 1
            return count

        while bricks[0] != 0:
            curedge = cut(bricks)
            last = fill(bricks, wall)
            if curedge > edge and not last:
                edge = curedge
            if edge == h:
                return 0

        return h - edge


# O(N)
class Solution2:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        for line in wall:
            i = 0
            while len(line) != 1:
                brick = line.pop()
                i += brick
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        if len(dic) == 0:
            return len(wall)
        return len(wall) - max(dic.values())
