from multiprocessing import Process, Pipe
from threading import Thread, get_ident

class Process_Wrapper:

    def __init__(self, instance):
        self.process = None
        self.threads = instance
        self.pub_pipe = None
        self.sub_pipe = None

    def start(self):
        self.pub_pipe, self.sub_pipe = Pipe()
        self.process = Process(target=self.threads.run, args=(self.sub_pipe, ))
        self.process.start()

    def stop(self):
        self.pub_pipe.send("stop request")
        print("stop request created")
        self.process.join()
        print("proess exit")

class Wrapped_Thread:

    def __init__(self):
        self._thread_one = None
        self._thread_two = None
        self._flag = True

    def start(self):
        self._thread_one = Thread(target=self.heavy_task)
        self._thread_two = Thread(target=self.heavy_task)
        self._thread_one.start()
        self._thread_two.start()

    def run(self, pipe: Pipe):
        self.start()

        # await stop_message
        msg = pipe.recv()
        pipe.close()
        print(msg)

        self.stop()

    def stop(self):
        self._flag = False
        self._thread_one.join()
        self._thread_two.join()

    def heavy_task(self):
        self.print_thread_info("start")
        while self._flag:
            pass
        self.print_thread_info("end")

    def print_thread_info(self, msg: str):
        print("[thread id: {}] {}".format(get_ident(), msg))
