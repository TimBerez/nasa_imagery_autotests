from behave import given, when, then
from behave import use_step_matcher

from assertions.api.earth.imagery_asserts import ImageryAsserts
from assertions.api.shared_asserts import SharedAsserts
from clients.api.default_params import get_default_imagery_request
from clients.api.earth_client import ApiEarthClient
from clients.api.models.imagery import ImageryRequest
from core.logger import Logger

logger = Logger()

use_step_matcher('re')


@given("we have default request params")
def step_impl(context):
    context.request_params = get_default_imagery_request(context)


@then("we get (.*) response status code")
def step_impl(context, status_code):
    _sharedAsserts = SharedAsserts()
    _sharedAsserts.assert_response_code(context.api_response, int(status_code))


@then("we assert img response (.*) to excepted pattern (.*)")
def step_impl(context, equals, pattern):
    _ImageryAsserts = ImageryAsserts()
    exc_pattern = _ImageryAsserts.get_excepted_pattern(pattern)
    if equals == 'equals':
        _ImageryAsserts.assert_response_img(context.api_response, exc_pattern, True)
    elif equals == 'not equals':
        _ImageryAsserts.assert_response_img(context.api_response, exc_pattern, False)
    else:
        raise Exception('Step is incorrect, please check args')


@when("we send request to imagery endpoint")
def step_impl(context):
    _ApiEarthClient = ApiEarthClient(context)
    context.api_response = _ApiEarthClient.get_imagery_results(ImageryRequest.parse_obj(context.request_params))
