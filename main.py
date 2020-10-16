from process import *
import time

threads = Wrapped_Thread()
process = Process_Wrapper(threads)
process.start()
time.sleep(5)
process.stop()
