import random

class TooSmallException(Exception):
    pass

class TooBigException(Exception):
    pass

class RightValueException(Exception):
    pass


secret_val = random.randint(0, 1000)
def guess(x):
    if x < secret_val:
        raise TooSmallException()
    elif x > secret_val:
        raise TooBigException()
    else:
        raise RightValueException()
        
