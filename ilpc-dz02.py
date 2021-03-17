from test import test

def my_test_function(start, stop, step, N):
    test_range = range(start, stop, step)
    for i in range(N):
        discard_value = i in test_range
    return

test(my_test_function, (0, 1000, 2, 10000), 20)
