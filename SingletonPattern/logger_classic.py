#This is the logging class, which follows the same pattern as singleton_classic
import datetime
class Logger(object):
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
            # this is how we ensure we only have one instance by doing reflection
        return Logger._instance

    def open_log(self, path):
        self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s %s' % (now, log_record)
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()

#let's test the logger
logger = Logger.instance()
logger.open_log('my.log')
logger.write_log('writing a log with the classic singleton pattern\n')
logger.write_log('****\n')
logger.close_log()

with open('my.log','r') as f:
    for line in f:
        print(line)