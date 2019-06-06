@login
Feature: This feature file will contain all tests related to login

  @login.valid @logout @tag1
  Scenario: ID-001
  [ This test case test the login functionality using valid credentials ]
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option


  @login.invalid @tag2
  Scenario: ID-002
  [ This test case test the login functionality using invalid user and password ]
    Given I login with username "invalid_user" and password "invalid_password"
    Then I should see exact text "Django administration"
    And I should see text "Please enter the correct username and password for a staff account"
    And I should see text "Note that both fields may be case-sensitive"
    But I should not see text "WELCOME"


  @login.invalid @tag3 @tag2
  Scenario: ID-003
  [ This test case test the login functionality using valid password but invalid password ]
    Given I login with username "invalid_user" and password "valid_password"
    Then I should see exact text "Django administration"
    And I should see text "Please enter the correct username and password for a staff account"
    And I should see text "Note that both fields may be case-sensitive"
    But I should not see text "WELCOME"


  @login.invalid @tag4
  Scenario: ID-004
  [ This test case test the login functionality using valid user but invalid password ]
    Given I login with username "valid_user" and password "invalid_password"
    Then I should see exact text "Django administration"
    And I should see text "Please enter the correct username and password for a staff account"
    And I should see text "Note that both fields may be case-sensitive"
    But I should not see text "WELCOME"