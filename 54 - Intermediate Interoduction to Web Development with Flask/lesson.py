import time
current_time = time.time()
print(current_time)

# Decarator Function


def speed_calc_decorator(func):
    def wrapper_function():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time-start_time}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
