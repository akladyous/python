import time
from timer_decorator import *


@timer_decorator
def prova():
    time.sleep(0.0001)
    return "test completed"


print(prova())
