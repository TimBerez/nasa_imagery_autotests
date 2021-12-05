from behave import then
from behave import use_step_matcher

from assertions.api.shared_asserts import SharedAsserts
from core.logger import Logger

logger = Logger()

use_step_matcher('re')


@then("we assert error message '(.*)' in response")
def step_impl(context, message):
    _sharedAsserts = SharedAsserts()
    _sharedAsserts.assert_response_body_error(context.api_response, message)
