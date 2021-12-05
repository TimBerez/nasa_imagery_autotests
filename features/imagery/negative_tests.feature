@negative @main_run
Feature: Negative imagery tests
  This tests check negative cases functionality of imagery endpoint


  Scenario: Future date raise api exception
    Given we set params for imagery request
      | param | value      |
      | date  | 2099-11-11 |
    When we send request to imagery endpoint
    Then we assert error message 'No imagery for specified date.' in response


  Scenario: Incorrect api key raise api exception
    Given we set params for imagery request
      | param   | value         |
      | api_key | not_exist_key |
    When we send request to imagery endpoint
    Then we assert error message 'An invalid api_key was supplied. Get one at https://api.nasa.gov:443' in response


  Scenario: Incorrect date key raise api exception
    Given we set params for imagery request
      | param | value |
      | date  | 11    |
    When we send request to imagery endpoint
    Then we assert error message 'time data '11' does not match format '%Y-%m-%d'. Allowed request fields for earth/imagery method are 'lat', 'lon', 'address', 'dataset', 'date', 'cloud_score', 'dim'' in response

  Scenario Outline: Incorrect lat key raise api exception
    Given we set params for imagery request
      | param     | value    |
      | <subject> | 99999999 |
    When we send request to imagery endpoint
    Then we assert error message 'value <subject> is incorrect' in response
    Examples:
      | subject |
      | lat     |
      | lon     |

