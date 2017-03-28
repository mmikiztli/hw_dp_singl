import time


class Logger:

    instance = None

    class __Logger:

        def __init__(self):
            self.file_name = "logfile_" + time.strftime("%Y_%m_%d_%H_%M_%S")
            self.create_file()

        def create_file(self):
            with open("%s.txt" % self.file_name, "w+") as log_file:
                return

        def log(self, message):
            with open("%s.txt" % self.file_name, "a+") as log_file:
                log_file.writelines(message + '\n')

    def __init__(self):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __getattr__(self, name):
        return getattr(self.instance, name)
