import time

def run_one_thread():
    thread_one = Sample_Thread()
    thread_one.start()
    time.sleep(5)
    thread_one.stop()

def run_two_threads():
    threads = Sample_Threads()
    threads.start()
    time.sleep(5)
    threads.stop()

if __name__ == "__main__":
    from thread import *
    run_one_thread()
    run_two_threads()
else:
    from .thread import *