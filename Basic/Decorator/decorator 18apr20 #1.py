# simple decorator -----------------------------
def decorator1(func):
    def inner():
        print('just before external function')
        func()
        print('just after external function')
    return inner


def func():
    print('function FUNC ±±±')

func=decorator1(func)
func()
