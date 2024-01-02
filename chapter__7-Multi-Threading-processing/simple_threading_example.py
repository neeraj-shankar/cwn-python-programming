from threading import *
import time
from helper_utilities.loggers import logger_setup

logger = logger_setup(__name__)
class A(Thread):

    def run(self):
        for _ in range(10):
            logger.info(f"Hi...")
            time.sleep(1)


class B(Thread):
    def run(self):
        for _ in range(10):
            logger.info(f"Hello...")
            time.sleep(1)


"""
Create object 
"""
t1 = A()
t2 = B()
t1.start()
t2.start()

print(f"End of process")
