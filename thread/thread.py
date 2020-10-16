from threading import Thread, get_ident, active_count

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

class Sample_Threads:

    def __init__(self):
        self.print_thread_num()
        self._thread_one = None
        self._thread_two = None
        self._flag = True
        self._data = None

    def start(self):
        self._thread_one = Thread(target=self.heavy_task)
        self._thread_two = Thread(target=self.heavy_task)
        self._thread_one.start()
        self._thread_two.start()
        self.print_thread_num()

    def stop(self):
        self._flag = False
        self._thread_one.join()
        self._thread_two.join()
        self.print_thread_num()

    def heavy_task(self):
        self.print_thread_info("start")
        self.set_data(str(get_ident()))
        self.print_thread_info("data is {}".format(self._data))
        while self._flag:
            pass
        self.print_thread_info("end")
        self.print_thread_info("data is {}".format(self._data))

    def set_data(self, msg: str):
        self._data = msg

    def print_thread_info(self, msg: str):
        print("[thread id: {}] {}".format(get_ident(), msg))

    def print_thread_num(self):
        print("thread num is {}".format(active_count()))