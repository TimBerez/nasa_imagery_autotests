import shutil
import requests

from assertions.api.shared_asserts import SharedAsserts
from core.logger import Logger

logger = Logger()


class ImageryAsserts(object):
    """Imagery endpoint assertions for tests"""
    _sharedAsserts = SharedAsserts()

    def get_excepted_pattern(self, pattern):
        excepted_body_dict = {
            'krasnodar_pattern_1': 'assertions/api/earth/imagery_png_patterns/krasnodar_pattern_1.png'
        }
        return excepted_body_dict[pattern]

    def assert_response_img(self, response: requests.Response, excepted_img_path: str, assertion: bool):
        try:
            self._sharedAsserts.assert_response_code(response, 200)
        except:
            raise Exception('Incorrect input data {}'.format(response.text))

        try:
            _tmp_file_path = 'temp/test_img.png'
            with open(_tmp_file_path, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            logger.info('Asserting response body with excepted')
            if assertion:
                assert self.validate_file_contents(_tmp_file_path, excepted_img_path)
            else:
                assert not self.validate_file_contents(_tmp_file_path, excepted_img_path)
        except:
            raise AssertionError('Assertion is failed')

    def validate_file_contents(self, file1, file2):
        with open(file1, 'r', errors='ignore') as f1, open(file2, 'r', errors='ignore') as f2:
            contents1 = f1.read()
            contents2 = f2.read()
        return contents1 == contents2
