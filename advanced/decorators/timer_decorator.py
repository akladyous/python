import time


def timer_decorator(callback):
    def decorator(*args, **kwargs):
        start_time = time.time()
        callback_result = callback(*args, **kwargs)
        end_time = time.time()

        elapsed_time = end_time - start_time

        time_units = {
            "seconds": elapsed_time,
            "milliseconds": elapsed_time * 1000,
            "microseconds": elapsed_time * 1e6,
        }
        if elapsed_time >= 1:
            unit = "seconds"
        elif elapsed_time >= 0.001:
            unit = "milliseconds"
        else:
            unit = "microseconds"

        print(f"Elapsed time: {time_units[unit]:.2f} {unit}")
        return callback_result

    return decorator
