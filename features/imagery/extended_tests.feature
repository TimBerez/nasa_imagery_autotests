@extended @main_run
Feature: Parametric imagery tests
  This tests check extended parmetric functionality of imagery endpoint


  Scenario: Early date request returns the same picture
    Given we set params for imagery request
      | param | value      |
      | date  | 2021-11-11 |
    When we send request to imagery endpoint
    Then we assert img response equals to excepted pattern krasnodar_pattern_1


  Scenario: Very early date request returns not the same picture
    Given we set params for imagery request
      | param | value      |
      | date  | 2021-09-11 |
    When we send request to imagery endpoint
    Then we assert img response not equals to excepted pattern krasnodar_pattern_1

  Scenario: Changing dim resolution goes to change picture
    Given we set params for imagery request
      | param | value |
      | dim   | 0.15  |
    When we send request to imagery endpoint
    Then we assert img response not equals to excepted pattern krasnodar_pattern_1

  Scenario Outline: Changing coordinate params goes to change picture
    Given we set params for imagery request
      | param | value |
      | lat   | <lat> |
      | lon   | <len> |
    When we send request to imagery endpoint
    Then we assert img response not equals to excepted pattern krasnodar_pattern_1

    Examples:
      | lat   | len   |
      | 46.02 | 39.01 |
      | 45.02 | 54.01 |
