# coding=utf-8
import sys, time, random, collections


def sample(numbers, rates):
    ratesum = sum(rates)
    r = random.uniform(0, ratesum)
    resi = -1
    tempr = 0
    for i in range(len(rates)):
        tempr += rates[i]
        if tempr > r:
            resi = i
            break
    resn = numbers.pop(resi)
    rates.pop(resi)
    return resn


import heapq
import random


def interviewQ(args):
    """
    :samples: [(item, weight), ...]
    :k: number of selected items
    :returns: [(item, weight), ...]
    """
    print(args)
    (samples, m) = args
    heap = []  # [(new_weight, item), ...]
    for sample in samples:
        wi = sample[1]
        ui = random.uniform(0, 1)
        ki = ui ** (1 / wi)

        if len(heap) < m:
            heapq.heappush(heap, (ki, sample))
        elif ki > heap[0][0]:
            heapq.heappush(heap, (ki, sample))

            if len(heap) > m:
                heapq.heappop(heap)

    return [item[1] for item in heap]


# def interviewQ(a):
#     (numberset, rates) = a
#     numberset = list(numberset)
#     rates = list(rates)
#     # print(numberset)
#     # print(rates)
#     select = 2
#     res = []
#     for i in range(select):
#         res.append(sample(numberset, rates))
#     return res


class Solution:
    TITLE = "Yuxin Zhang Interview..."

    def run(self, inputs, expects, algo, collect=[]):
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
            collect.append(self.test(pair, algo))

    def test(self, pair, algo):
        startTS = time.time()
        res = algo(pair[0])
        endTS = time.time()
        timespend = endTS - startTS
        # print(
        #     "Actual       : "
        #     + str(res)
        #     + " \nExpected  : "
        #     + str(pair[1])
        #     + " \ntimespent : "
        #     + str(timespend)
        # )
        return res


# input1 = [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50, 100]
input1 = ([(1, 10), (2, 20), (3, 30), (4, 40), (5, 100)], 3)
expected1 = 4

input2 = [1, 1, 2], 3, []
expected2 = 4

input3 = [4, 3, 2], 2, []
expected3 = 9

inputset = [input1]
expectedset = [expected1]
test = Solution()
collector = []
for i in range(250000):
    test.run(inputset, expectedset, interviewQ, collect=collector)

dic = collections.defaultdict(int)
for li in collector:
    for n in li:
        dic[n] += 1
print(dic)
for i in range(5):
    print(dic[i])
