from abc import ABCMeta, abstractmethod
from collections import namedtuple


class ILogger(metaclass=ABCMeta):

    @abstractmethod
    def log_message(self, msg):
        pass

    @abstractmethod
    def log_error(self, msg):
        pass

    @abstractmethod
    def log_info(self, msg):
        pass

class LogToFile(ILogger):
    def log_message(self, msg):
        print("[ok] to file %s" % msg)

    def log_error(self, msg):
        print("[error] to file %s" % msg)

    def log_info(self, msg):
        print("[info] to file %s" % msg)

class LogToKibana(ILogger):
    def log_message(self, msg):
        print("[ok] to kibana %s" % msg)

    def log_error(self, msg):
        print("[error] to kibana %s" % msg)

    def log_info(self, msg):
        print("[info] to kibana %s" % msg)


class LoggerProviderFactory(object):
    @staticmethod
    def get_loggin_provider(providers):
        if providers == 'file':
            return LogToFile()
        elif providers == 'kibana':
            return LogToKibana()
        else:
            return LogToFile()

if __name__ == '__main__':

    logges = LoggerProviderFactory.get_loggin_provider('file')
    logges.log_message("test")
    logges.log_error("test")
    logges.log_info("test")

    logges = LoggerProviderFactory.get_loggin_provider('kibana')
    logges.log_message("test")
    logges.log_error("test")
    logges.log_info("test")
