from behave import given, when, then
from behave import use_step_matcher

from assertions.api.shared_asserts import SharedAsserts
from clients.api.earth_client import ApiEarthClient
from clients.api.models.imagery import ImageryRequest
from assertions.api.earth import imagery_asserts
from core.logger import Logger
from clients.api.default_params import get_default_imagery_request
logger = Logger()

use_step_matcher('re')


@given("we set params for imagery request")
def step_impl(context, datatable='||'):
    pass


@given("we have default request params")
def step_impl(context):
    context.request_params = get_default_imagery_request(context)


@then("we get (.*) response status code")
def step_impl(context, status_code):
    _sharedAsserts = SharedAsserts()
    _sharedAsserts.assert_response_code(context.api_response, int(status_code))


@when("we send request to imagery endpoint")
def step_impl(context):
    _ApiEarthClient = ApiEarthClient(context)
    context.api_response = _ApiEarthClient.get_imagery_results(ImageryRequest.parse_obj(context.request_params))
