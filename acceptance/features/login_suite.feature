@login
Feature: This feature file will contain all tests related to login

  @login.valid @logout @tag1
  Scenario: ID-001
  [ This test case test the login functionality using valid credentials ]
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option