

def question1(listoflists):
    nlist = len(listoflists)
    res = []
    index = 0
    maxlen = 0
    for i in range(nlist):
        maxlen = max(maxlen, len(listoflists[i]))

    while index < maxlen:
        for i in range(nlist):
            li = listoflists[i]
            if index < len(li):
                res.append(li[index])
        index += 1

    return res


test1 = [[1, 2, 3], [4, 5, 6], [7, 8]]

print(question1(test1))





def patchprocess(urls, webproccer):

    dictionary = {}

    for url in urls:

        startMultithread(url, webproceer, dictionary, finishprocessing)

    wait finishprocessing
        return dictionary
