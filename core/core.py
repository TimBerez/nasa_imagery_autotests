from os.path import normpath

import yaml
from munch import Munch

from core.logger import Logger

logger = Logger()


class AppConfig:
    _instance = None
    _CONFIG_PATH = "core/config.yml"

    def __new__(cls):
        if not cls._instance:
            with open(normpath(cls._CONFIG_PATH)) as config_file:
                full_config = yaml.safe_load(config_file)

            cls._instance = cls._make_objectable(full_config)
            logger.debug(
                'AppConfig: application config successfully loaded. Config:'
                ' %s', cls._instance
            )

        return cls._instance

    @classmethod
    def _make_objectable(cls, input_dict):
        temp_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, dict):
                temp_dict[key] = cls._make_objectable(value)
            else:
                temp_dict[key] = value
        return Munch(temp_dict)
