import time

def run_one_process():
    process = Sample_Process()
    process.start()
    time.sleep(5)
    process.stop()

if __name__ == "__main__":
    from process import *
    from process_wrapper import *
    run_one_process()
else:
    from .process import *
    from .process_wrapper import *