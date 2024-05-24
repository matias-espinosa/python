import datetime
import functools

def log_en_archivo(file_path, log_message_template):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the current date and time
            now = datetime.datetime.now()
            # Merge args and kwargs into a dictionary for easier access
            func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
            args_dict = dict(zip(func_args, args))
            args_dict.update(kwargs)
            # Format the log message using the template
            log_message = log_message_template.format(now=now, **args_dict)
            # Write the log message to the file
            with open(file_path, "a") as f:
                f.write(log_message)
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator
