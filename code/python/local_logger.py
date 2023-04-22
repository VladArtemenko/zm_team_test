import logging


class LocalLogger:
    def __init__(self, name, log_level=logging.DEBUG):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(log_level)

        formatter = logging.Formatter(
            fmt='[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] [Process=%(process)s] %(message)s',
            datefmt="%d/%b/%Y %H:%M:%S"
        )

        file_handler = logging.FileHandler('./logs/logfile.log', mode='a')
        file_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(stream_handler)

    @property
    def writer(self):
        return self._logger