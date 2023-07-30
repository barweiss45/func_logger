# func_logger - A logger for functions

## Overview

This Python logging module provides a decorator function called `log_output` that can be used to log the output of any function it decorates. The decorator logs the function call details, including arguments, output, and the file path of the module where the function is defined. The log messages can be customized with different log levels and are useful for monitoring and debugging your Python scripts.

## Installation

To use this logging module, follow these steps:

1. Download the `func_logger.py` file and place it in your project directory. Use git, copy it, download, etc.
2. Make sure you have Python installed on your system.

## Usage

1. Import the `configure_logging` function, and the `log_output` decorator from the `func_logger` module in your Python script:

    ```python
    from func_logger import configure_logging, log_output
    ```

2. Decorate any function that you want to log using the log_output decorator. You can provide a custom log level (optional) as an argument to the decorator. If no log level is provided, it will default to logging.INFO.

    ```python

    configure_logging()

    @log_output(log_level='info')
    def my_function(arg1, arg2):
        # Your function code here
        return some_result
    ```

3. Now, when you call my_function, the decorator will log the function call details, including arguments and output, along with the file path of the module where my_function is defined.

## Example

Here's an example of how the logging module can be used in your Python script. This will send all output for a function that is set at `warning` or hider to a file called `my_logs` and to the stdout:

```python
from func_logger import log_output, configure_logging

configure_logging(filename='my_logs', level='warning')

@log_output(log_level='warning')
def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 0)
```

In this example, the divide_numbers function is decorated with `log_output(log_level='warning')`. The log message will include the log level, function call details, and the file path of the module where divide_numbers is defined.

## Log Levels

This logging module supports different log levels for the log messages. This module is built so you don't need to add any more code to your script than necessary. So you don't need to import the logging module where you don't need too. All log levels values for the attribute of both functions can be used as a string. 

The available log levels are:

* `debug`: Detailed information, typically used for debugging purposes.
* `info`: General information about the program's operation.
* `warning`: Warning messages, indicating potential issues but not critical errors.
* `error`: Error messages, indicating a critical error that might require attention.
* `critical`: Critical error messages, indicating a severe error that might lead to program termination.

## Contributions
Contributions to this logging module are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or a pull request on the repository.