import time

class HowMuchTime:

    def __init__(self):
      self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self,*args):
        self.get_time()

    def get_time(self):
        print(time.time() - self.start)

with HowMuchTime() as t:
    time.sleep(3)
    t.get_time()
    time.sleep(2)