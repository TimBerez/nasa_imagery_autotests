from behave import given, when, then
from behave import use_step_matcher

from assertions.api.shared_asserts import SharedAsserts
from clients.api.earth_client import ApiEarthClient
from clients.api.models.imagery import ImageryRequest
from assertions.api.earth.imagery_asserts import ImageryAsserts
from core.logger import Logger
from clients.api.default_params import get_default_imagery_request
logger = Logger()

use_step_matcher('re')


@given("we set params for imagery request")
def step_impl(context, datatable='||'):
    params = get_default_imagery_request(context)
    for row in context.table:
        params.update({row[0]: row[1]})
        logger.info('We set params for request {}'.format(params))
        context.request_params = params
