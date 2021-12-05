"""Logging stuff."""
import logging
import logging.config
import os
import os.path
import sys
from glob import glob
from uuid import uuid4

from munch import Munch


class Logger():
    _formatter = None
    _instance = None
    _message_format = '\n%(asctime)s\n%(levelname)s %(name)s: %(message)s'
    _timestamp_format = '%d.%m.%Y %H:%M:%S'
    _file_path = 'tests.log'
    _temp_file_path = 'temp/'
    _main_log_level = logging.DEBUG
    _scenario_log_level = logging.DEBUG

    def __new__(cls):

        if not cls._instance:
            cls._instance = cls._initialize_logging()
        return cls._instance

    @classmethod
    def _initialize_logging(cls):
        """Initialize logging."""

        logger = logging.getLogger('nasa_tests')
        cls.formatter = logging.Formatter(
            cls._message_format, cls._timestamp_format
        )
        file_handler = logging.FileHandler(cls._file_path)
        file_handler.setFormatter(cls.formatter)
        file_handler.setLevel(cls._main_log_level)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(cls.formatter)
        console_handler.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        logger.handlers = []
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger

    @classmethod
    def add_temp_file_handler(cls, logger):
        """Adds file handler and returns handler object.

        File handler supposed to be used temporary and then be removed. For
        example during one sceration.
        """

        log_path = os.path.join(cls._temp_file_path, '{}.log'.format(uuid4()))
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(cls._formatter)
        file_handler.setLevel(cls._scenario_log_level)
        logger.addHandler(file_handler)
        return Munch({'handler': file_handler, 'path': log_path})

    @classmethod
    def clean_temp_folder(cls, logger):
        """Clean folder with temp log files."""

        for temp_file in glob(os.path.join(cls._temp_file_path, '*.log')):
            try:
                os.remove(temp_file)
            except Exception:
                logger.exception(
                    'Failed to remove temp log file %s', temp_file,
                    exc_info=True
                )
