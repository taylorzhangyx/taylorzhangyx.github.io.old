

#
# Your previous Plain Text content is preserved below:
#
#
# Boolean search is powerful in sourcing and recruiting.
# We will use machine learning prediction to provide relations among skills. Now we need a function to transfer those relations to a string with correct boolean format.
#
# Example1:
# input: [["java", "python"], ["machine learning", "deep learning"]]
# output: ("java" OR "python") AND ("machine learning" OR "deep learning")
#
# Example2:
# input: [[["java", "maven", "spring"], "python"], ["machine learning", "deep learning"]]
# output: (("java" OR "maven" OR "spring") AND "python") AND ("machine learning" OR "deep learning")


def generateStr(hasnested, res):
    seperator = " AND " if hasnested else " OR "

    resstring = seperator.join(iter(res)) # "java" OR "maven" OR "spring"

    return "(" + resstring + ")"

def processItem(item, res):
    hasnested = False
    if type(item) == list:
        res.append(transform(item))
        hasnested = True
    else:
        res.append(item)
    return hasnested

def transform(inputs):

    res = []
    hasnested = False
    for item in inputs:
        while type(item) == list and len(item) == 1:
            item = item[0]

        hasnested =  processItem(item, res) or hasnested

    return generateStr(hasnested, res)


print(transform([[["java", "maven", "spring"], "python"], ["machine learning", "deep learning"]]))
