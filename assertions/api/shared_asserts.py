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

    def assert_response_body(self, response: requests.Response, excepted_body: any):
        try:
            logger.info('Asserting response body equals {}'.format(excepted_body))
            assert response.text == excepted_body
        except:
            raise Exception('Current body is {} excepted {}'.format(response.status_code, excepted_body))
