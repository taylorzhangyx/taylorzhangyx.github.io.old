# coding=utf-8
import sys, time


def interviewQ(a):
    (m, n, i) = a
    print(m)
    print(n)
    print(i)
    return


class Solution:
    TITLE = "Yuxin Zhang Interview..."

    def run(self, inputs, expects, algo):
        print(self.TITLE)

        ilen = len(inputs)
        elen = len(expects)

        if ilen != elen:
            print(
                "Input ERROR, the inputs length and expects length are not identical."
            )
            return

        for i in range(ilen):
            pair = (inputs[i], expects[i])
            self.test(pair, algo)

    def test(self, pair, algo):
        startTS = time.time()
        res = algo(pair[0])
        endTS = time.time()
        timespend = endTS - startTS
        print(
            "Actual       : "
            + str(res)
            + " \nExpected  : "
            + str(pair[1])
            + " \ntimespent : "
            + str(timespend)
        )


input1 = [1], 3, [4, 2, 4, 6]
expected1 = 4

input2 = [1, 1, 2], 3, []
expected2 = 4

input3 = [4, 3, 2], 2, []
expected3 = 9

inputset = [input1, input2, input3]
expectedset = [expected1, expected2, expected3]
test = Solution()
test.run(inputset, expectedset, interviewQ)
