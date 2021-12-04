from behave import given, when, then
from behave import use_step_matcher
from clients.api.earth_client import ApiEarthClient
from clients.api.models.imagery import ImageryRequest

from core.logger import Logger

logger = Logger()

use_step_matcher('re')

@given("we set params for imagery request")
def step_impl(context, datatable='||'):
    pass

@given("we have default request params")
def step_impl(context):
    context.request_params = {'lat': 45.02,
                              'lon': 39.01,
                              'dim': 0.0001,
                              'date': '2021-11-13',
                              'cloud_score': False,
                              'api_key': context.app_config.api_host}

@then("we get (.*) response status code")
def step_impl(context, status_code):
    pass

@when("we send request to imagery endpoint")
def step_impl(context):
    _ApiEarthClient = ApiEarthClient(context)
    _ApiEarthClient.get_imagery_results(ImageryRequest.parse_obj(context.request_params))



