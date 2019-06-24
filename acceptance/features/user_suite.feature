@users
  Feature: This suite will contain all the tests related to user management

  @users.add_successful
  Scenario: 001
    [This test case adds a new user]
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option
    When I click on Add option on Users dashboard
    Then Add user page is displayed
    When I create a new user with the following information
      | username | password   | password_confirmation |
      | test_1   | pass123!!  | pass123!!             |
    And I click on SAVE button
    Then Edit user information page is loaded
    When I click on SAVE button again
    Then Select user to change page is displayed
    When I write "search_user" on search box
    Then I see "search_user" displayed on results grid