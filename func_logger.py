import logging

'''
Add to modules with functions to log:

from func_logger import configure_logging, log_output

configure_logging(f"{__name__}-langchain.log")

@log_output
def func(x,y):
    return output

'''

def log_configure_map(level):

    log_level = {

        "debug": logging.DEBUG,
        "info": logging.INFO,
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
    }

    return log_level[level]

def log_output_map(level):

    log_level = {

        "debug": logging.debug,
        "info": logging.info,
        "critical": logging.critical,
        "error": logging.error,
        "warning": logging.warning,
    }

    return log_level[level]

def configure_logging(log_filename="langlogger.log", level='info'):
    
    level = log_configure_map(level)

    # Configure the root logger
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create a handler to log to stdout (console)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a handler to log to a file in the CWD
    file_handler = logging.FileHandler(filename=log_filename)
    file_handler.setLevel(level)

    # Define the formatter for both handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the root logger
    logger = logging.getLogger('')
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def log_output(level='info'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = log_output_map(level)
            result = func(*args, **kwargs)
            file_path = func.__module__.__file__
            log(f"Function 'Function '{func.__name__}' from module '{file_path}' called with arguments: {args}, {kwargs}. Output: {result}")
            return result
        return wrapper
    return decorator