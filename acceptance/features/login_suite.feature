Feature: This feature file will contain all tests related to login

  @wip
  Scenario:
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option