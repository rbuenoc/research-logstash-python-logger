from logging import (getLogger, FileHandler, StreamHandler,
                     Formatter, error, exception, info, warning,
                     getLogger, getLogRecordFactory, setLogRecordFactory)
from logstash_async.handler import AsynchronousLogstashHandler
from logging.handlers import RotatingFileHandler


LOG_FILE = 'app.log'
LOG_FORMAT = '%(asctime)s %(version)s %(levelname)s - %(name)s - %(message)s'

root_logger = getLogger()


_former_log_record_factory = getLogRecordFactory()

def _version_log_record_factory(*args, **kwargs):
    record = _former_log_record_factory(*args, **kwargs)
    record.version = 'default'
    return record


def initialize_logging():
    root_logger.setLevel('DEBUG')
    formatter = Formatter(LOG_FORMAT)

    #file_handler = FileHandler(filename=LOG_FILE, mode='w')
    #file_handler.setLevel('ERROR')
    #file_handler.setFormatter(Formatter(LOG_FORMAT))
    #root_logger.addHandler(file_handler)

    console_handler = StreamHandler()
    console_handler.setLevel('INFO')
    console_handler.setFormatter(Formatter(LOG_FORMAT))
    root_logger.addHandler(console_handler)

    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=150, backupCount=4)
    rotating_handler.setLevel('INFO')
    rotating_handler.setFormatter(Formatter(LOG_FORMAT))
    root_logger.addHandler(rotating_handler)

    #logstash_handler = AsynchronousLogstashHandler(host='localhost', port=5000, database_path=None)
    #logstash_handler.setLevel('INFO')
    #logstash_handler.setFormatter(Formatter(LOG_FORMAT))
    #root_logger.addHandler(logstash_handler)

    setLogRecordFactory(_version_log_record_factory)


def log_info(name, message, *args, **kwargs):
    logger = _get_logger(name)
    logger.info(message, *args, **kwargs)


def log_error(name, message, *args, **kwargs):
    logger = _get_logger(name)
    logger.error(message, *args, **kwargs)


def log_exception(name, message, *args, **kwargs):
    logger = _get_logger(name)
    logger.exception(message, *args, **kwargs)


def log_critical(name, message, *args, **kwargs):
    logger = _get_logger(name)
    logger.critical(message, *args, **kwargs)


def log_warning(name, message, *args, **kwargs):
    logger = _get_logger(name)
    logger.warning(message, *args, **kwargs)


def _get_logger(name):
    return getLogger(name)
