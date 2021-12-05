@smoke @main_run
Feature: Smoke imagery tests
  This tests check smoke functionality of imagery endpoint

  Scenario: Get basic response with default params
    Given we have default request params
    When we send request to imagery endpoint
    Then we get 200 response status code

  Scenario: Assert basic response with default params
    Given we have default request params
    When we send request to imagery endpoint
    Then we assert img response equals to excepted pattern krasnodar_pattern_1