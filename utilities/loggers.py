"""
A simple python program to enable logging feature
"""
import logging
import threading
import multiprocessing

def logger_setup(name):

    # format and log details
    log_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] [Thread:%(thread)d] [Process:%("
                                      "process)d] %(message)s", "%Y-%m-%d %H:%M:%S")

    # to add logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    # setting log handler and log level
    logger = logging.getLogger()
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    return logger
