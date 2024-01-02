"""
A simple python program to demonstrate the multiple threading
"""
import time
import threading

# Creating two threads
program_start_time = time.time()
print(program_start_time)
time_struct = time.localtime(program_start_time)
print(f"The program start time in local --> {time_struct}")
time_24_hour_format = time.strftime("%H:%M:%S", time_struct)
print(f"The time after conversion in 24-hour format --> {time_24_hour_format}")

# time_obj = time.strptime(str(program_start_time), "%H:%M:%S.%f")[:-3]

thread_time = time.thread_time()
print(f"The thread time --> {thread_time}")
t1 = threading.Thread(target=lambda x: x*x, args=(10,))
t2 = threading.Thread(target=lambda x: x**3, args=(10,))

