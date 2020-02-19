from threading import Thread


class Process(Thread):
    def __init__(self, name, callback):
        Thread.__init__(self)
        self.name = name
        self.callback = callback

    def run(self):
        self.callback()
        msg = "%s is running" % self.name
        print(msg)

