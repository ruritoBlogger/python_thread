from process import *
import time

process = Process_Wrapper()
process.start()
time.sleep(5)
process.stop()
