import datetime
import functools

def log_en_archivo(file_path, log_message_template):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
            args_dict = dict(zip(func_args, args))
            args_dict.update(kwargs)
            log_message = log_message_template.format(now=now, **args_dict)
            with open(file_path, "a") as f:
                f.write(log_message)
            return func(*args, **kwargs)
        return wrapper
    return decorador
