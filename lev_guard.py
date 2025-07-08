import functools

class HarmThresholdExceeded(Exception):
    pass

def LevGuard(harm_threshold=0.001):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            simulated_harm = kwargs.get("simulated_harm", 0.0)
            if simulated_harm > harm_threshold:
                raise HarmThresholdExceeded(
                    f"Aborted: Harm probability {simulated_harm} > threshold {harm_threshold}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator
