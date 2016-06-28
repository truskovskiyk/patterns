import threading


class LoggerSingleton(object):
    __instance = None
    __lock = threading.Lock()
    __count = 0

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = cls()
        return cls.__instance

    def log(self, msg):
        print("[log] [%s] : %s" % (self.__count, msg))
        with self.__lock:
            self.__count += 1

if __name__ == '__main__':
    l1 = LoggerSingleton.instance()
    for i in range(5):
        l1.log(5)
    l2 = LoggerSingleton.instance()
    for i in range(5):
        l2.log(5)
