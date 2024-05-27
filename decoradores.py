import datetime
import functools

def log_en_archivo(file_path, loguear_mensaje_template):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
            args_dict = dict(zip(func_args, args))
            args_dict.update(kwargs)
            loguear_mensaje = loguear_mensaje_template.format(now=now, **args_dict)
            with open(file_path, "a") as f:
                f.write(loguear_mensaje)
            return func(*args, **kwargs)
        return wrapper
    return decorador
