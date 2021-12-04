# Created by deski at 04.12.2021
Feature: Smoke imagery tests
  This tests check smoke functionality of imagery endpoint

  @run
  Scenario: Get basic response with default params
    Given we have default request params
    When we send request to imagery endpoint
    Then we get 200 response status code
