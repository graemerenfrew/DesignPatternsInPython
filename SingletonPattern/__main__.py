from logger_meta import Logger

logger = Logger('my.log')
logger.write_log('Logging with classic Singleton pattern\n')
logger2 = Logger('***ignored*** - the file should already be open')
logger2.write_log('Another log record\n')

logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')
