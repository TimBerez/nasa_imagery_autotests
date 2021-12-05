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


@then("we assert error message '(.*)' in response")
def step_impl(context, message):
    _sharedAsserts = SharedAsserts()
    _sharedAsserts.assert_response_body_error(context.api_response, message)
