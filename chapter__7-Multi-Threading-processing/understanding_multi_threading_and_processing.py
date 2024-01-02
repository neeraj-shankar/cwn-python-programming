import threading
import multiprocessing


def worker():
    print("Worker function running.")


if __name__ == "__main__":
    # Multi-threading example
    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=worker)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # Multiprocessing example
    process1 = multiprocessing.Process(target=worker)
    process2 = multiprocessing.Process(target=worker)
    process1.start()
    process2.start()
    process1.join()
    process2.join()


