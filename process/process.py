from threading import Thread, get_ident, active_count
from multiprocessing import Process

class Sample_Process:

    def __init__(self):
        self._process = None
        self._flag = True
        self._data = None

    def start(self):
        self._data = "nothing"
        self._process = Process(target=self.heavy_task)
        self._data = "before process"
        self._process.start()

    def stop(self):
        self._flag = False
        self._process.terminate()
        print(self._data) # before process

    def heavy_task(self):
        print(self._data) # before process
        self._data = "on process"
        print(self._data) # on process
        self.print_process_info("start")
        while self._flag:
            pass

    def print_process_info(self, msg: str):
        print("[process id: {}] {}".format(self._process.pid, msg))