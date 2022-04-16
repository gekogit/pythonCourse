import time


def timepassed(func):
    def inside_f():
        start = time.perf_counter()
        func()
        stop = time.perf_counter()
        print(f"Time needed: {stop - start} seconds")
    return inside_f


@timepassed
def test_f():
    print("Hahaha")


test_f()

