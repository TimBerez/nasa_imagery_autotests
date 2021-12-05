from urllib.parse import urljoin

import requests

from clients.api.models.imagery import ImageryRequest
from core.logger import Logger

logger = Logger()


def get_default_imagery_request(context):
    params = {'lat': 45.02,
              'lon': 39.01,
              'dim': 0.1,
              'date': '2021-11-13',
              'cloud_score': False,
              'api_key': context.app_config.api_key}
    return params
