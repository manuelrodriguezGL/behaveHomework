@users
Feature: This suite will contain all the tests related to user management

  @users.add_successful @logout
  Scenario: 001
  [This test case adds a new user]
    Given I login with username "admin" and password "admin"
    Then I should see logout option
    And I should see change password option
    When I click on Add option on Users dashboard
    Then I see the page header with text "Site administration"
    When I create a new user with the following information
      | username | password  | password_confirmation |
      | test_001 | pass123!! | pass123!!             |
    And I click on SAVE button
    Then I see the page header with text "Change user"
    When I click on SAVE button again
    Then I see the page header with text "Select user to change"
    When I search for "test_001" on search box
    Then I see "test_001" displayed on results grid
    And  I logout the application

  @users.remove_successful @duplicate
  Scenario: 002
  [This test case removes an existing user]
    Given I login with username "admin" and password "admin"
    Then I should see logout option
    And I should see change password option
    When I click on Add option on Users dashboard
    Then I see the page header with text "Site administration"
    When I create a new user with the following information
      | username | password  | password_confirmation |
      | test_002 | pass123!! | pass123!!             |
    And I click on SAVE button
    Then I see the page header with text "Change user"
    When I click on SAVE button again
    Then I see the page header with text "Select user to change"
    When I search for "test_002" on search box
    Then I see "test_002" displayed on results grid