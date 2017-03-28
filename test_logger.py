import unittest
import os.path
import logger


class LoggerTests(unittest.TestCase):

    def testFileExists(self):
        logger_one = logger.Logger()
        result = os.path.exists("%s.txt" % logger_one.file_name)
        self.assertEqual(result, True)

    def testSingleton(self):
        logger_one = logger.Logger()
        logger_two = logger.Logger()
        if logger_one == logger_two:
            result = True
        else:
            result = False
        self.assertEqual(result, True)

    def testLoggerMessage(self):
        logger_one = logger.Logger()
        message = logger_one.log("message")
        with open("%s.txt" % logger_one.file_name) as f:
            rows = f.readlines()
        lines = [line.strip("\n") for line in rows]
        result = "message" in lines
        self.assertEqual(result, True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
