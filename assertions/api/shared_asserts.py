import json
import shutil

import requests
from core.logger import Logger

logger = Logger()


class SharedAsserts(object):
    """Shared endpoint assertions for tests"""

    def assert_response_code(self, response: requests.Response, excepted_status_code: int):
        try:
            logger.info('Asserting response code equals {}'.format(excepted_status_code))
            assert response.status_code == excepted_status_code
        except:
            raise Exception('Current status code is {} excepted {}'.format(response.status_code, excepted_status_code))

    def assert_response_body_error(self, response: requests.Response, excepted_err: str):
        try:
            err = json.loads(response.text)['msg']
        except:
            err = json.loads(response.text)['error']['message']
        logger.info('Get error from response body {}'.format(err))
        try:
            logger.info('Asserting response err equals {}'.format(excepted_err))
            assert err == excepted_err
        except:
            raise Exception('Current err is {} excepted {}'.format(err, excepted_err))
