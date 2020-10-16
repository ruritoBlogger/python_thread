from threading import Thread, get_ident

class Sample_Thread:

    def __init__(self):
        self._thread = None
        self._flag = True

    def start(self):
        self._thread = Thread(target=self.heavy_task)
        self._thread.start()

    def stop(self):
        self._flag = False
        self._thread.join()

    def heavy_task(self):
        self.print_thread_info("start")
        while self._flag:
            pass
        self.print_thread_info("end")

    def print_thread_info(self, msg: str):
        print("[thread id: {}] {}".format(get_ident(), msg))