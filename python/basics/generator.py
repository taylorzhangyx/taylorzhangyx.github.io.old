# If a function contains yield, it becomes generator automatically
def fib(n):
    a = b = 1
    count = 0
    while count < n:
        a, b = b, a + b
        yield a
        count += 1


for x in fib(10):
    print(x)


# One good use case for the negerator is when we process the streams
# With generator, we don't have to process the whole stream then start dealing with the results
import random as r


class Stream:
    def __init__(self):
        self.data = [r.randrange(999) for i in range(2999)]


def getUniq(s: Stream) -> int:
    st = set()
    for x in s.data:
        if x not in st:
            ## with this yield, we don't have to finish going through the stream to output the valid results
            yield (x)
        st.add(x)


s = Stream()
for x in getUniq(s):
    print(x)
