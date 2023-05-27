
class IterLoop:
    def __init__(self, iterable):
        self._iterable = iterable
        self._IterObj  = iter(self._iterable)
    
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                NextObj = next(self._IterObj)
                return NextObj
            except StopIteration:
                self._IterObj = iter(self._iterable)


cl=IterLoop([1,2,3,4])
for x in range(5):
    print(next(cl))
print(next(cl))
print(next(cl))
