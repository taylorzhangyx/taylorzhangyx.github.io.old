class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        l = len(cells)

        mapRtoN = {}
        mapNtoR = {}

        mapRtoN[self.hash(cells)] = 0
        mapNtoR[0] = cells

        nc = cells
        for i in range(1, N + 1):
            nc = self.nextCell(nc)
            # check if this res appeared
            hashc = self.hash(nc)
            if hashc in mapRtoN.keys():
                # if yes, fold the loop
                return self.foldLoop(hashc, i, N, mapRtoN, mapNtoR)
            # if no, save res, continue
            else:
                mapRtoN[hashc] = i
                mapNtoR[i] = nc
        return nc

    def foldLoop(self, hashc, i, N, mapRtoN, mapNtoR):
        oldi = mapRtoN[hashc]
        looplen = i - oldi
        left = N - i
        resi = left % looplen + oldi
        return mapNtoR[resi]

    def hash(self, cells):
        return str(cells)

    def nextCell(self, cells):
        nextc = []

        def getC(cells, i):
            if i >= 0 and i < len(cells):
                return cells[i]
            else:
                return None

        for i in range(len(cells)):
            left = getC(cells, i - 1)
            right = getC(cells, i + 1)
            if left == None or right == None or left + right == 1:
                nextc.append(0)
            else:
                nextc.append(1)
        return nextc
