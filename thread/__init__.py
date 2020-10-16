import time

def run_one_thread():
    thread_one = Sample_Threads()
    # thread_one = Sample_Thread()
    thread_one.start()
    time.sleep(5)
    thread_one.stop()

if __name__ == "__main__":
    from thread import *
    run_one_thread()
else:
    from .thread import *