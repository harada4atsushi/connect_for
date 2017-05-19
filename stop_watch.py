from functools import wraps
import time

def stop_watch(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        elapsed_time =  time.time() - start
        func_name = func.__name__
        print("%s processing time: %s [sec]" % (func_name, elapsed_time))
        return result
    return wrapper