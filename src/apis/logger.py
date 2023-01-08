import logging
import os
from logging.handlers import RotatingFileHandler
from configs.app_configs import app_config


class AppLogger:
    _logger = None

    def __init__(self):
        self.call = True

    def get_logger(self, logger_name=app_config.app_name):
        if self._logger is None:
            self._logger = logging.getLogger(logger_name)
            self._logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            if app_config.env == 'local':
                sh = logging.StreamHandler()
                sh.setFormatter(formatter)
                self._logger.addHandler(sh)
            else:
                rotating_logs = RotatingFileHandler("env['APP_DIR']/log/{}.log".format(logger_name), maxBytes=50*1024*1024*8, backupCount=5)
                rotating_logs.setFormatter(formatter)
                self._logger.addHandler(rotating_logs)
        return self._logger

logger = AppLogger()