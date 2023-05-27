l1=list(range(1,4))

class CustomIter:
    def __init__(self, iterable):
        self._iterable = iterable
        #self._IterObj = iter(self._iterable)
    def __iter__(self):
        yield self._iterable
    # def __next__(self):
    #     while True:
    #         try:
    #             value = next(self._IterObj)
    #             return value
    #         except StopIteration:
    #             return False

i=CustomIter(l1)
for x in range(6):
    print(next)


