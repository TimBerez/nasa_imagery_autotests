from urllib.parse import urljoin

import requests

from clients.api.models.imagery import ImageryRequest
from core.logger import Logger

logger = Logger()


class ApiEarthClient(object):
    """Earth nasa endpoint client."""

    _imagery_endpoint = '/planetary/earth/imagery'

    def __init__(self, context):
        self.api_host = context.app_config.api_host
        self.api_key = context.app_config.api_key

    def get_imagery_results(self, params: ImageryRequest):
        url = urljoin(self.api_host, self._imagery_endpoint)
        query = params.dict()
        logger.info('We send req with parameters %s', query)
        response = requests.get(url, params=query, stream=True)
        return response
