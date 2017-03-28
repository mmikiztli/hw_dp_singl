import unittest
import os.path
import logger
import time


class LoggerTests(unittest.TestCase):

    def testLoggerType(self):
        logger_one = logger.Logger()
        result = type(logger_one).__name__
        self.assertEqual(result, 'Logger')

    def testLoggerMessage(self):
        logger_one = logger.Logger()
        result = hasattr(logger_one, "log")
        self.assertEqual(result, True)

    def testFileExists(self):
        logger_one = logger.Logger()
        result = os.path.exists("%s.txt" % logger_one.file_name)
        self.assertEqual(result, True)

    def testFileName(self):
        logger_one = logger.Logger()
        date_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        file_name = logger_one.file_name
        self.assertEqual(file_name, date_time)

    def testLoggerSingleton(self):
        logger_one = logger.Logger()
        message_one = logger_one.log("message_one")
        logger_two = logger.Logger()
        message_two = logger_two.log("message_two")
        with open("%s.txt" % logger_one.file_name) as f:
            rows = f.readlines()
        lines = [line.strip("\n") for line in rows]
        if "message_two" and "message_one" in lines:
            result = True
        else:
            result = False
        self.assertEqual(result, True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
