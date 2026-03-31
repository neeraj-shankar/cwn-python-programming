

## FAQs

### 1. How can we acheive true parrelalism using multithreading in python?
- In CPython, multithreading cannot achieve true parallelism for CPU-bound tasks due to the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time. 
- True parallelism can be achieved using multiprocessing, native extensions that release the GIL, or by using alternative Python runtimes without a GIL. Threads are still useful for I/O-bound workloads.