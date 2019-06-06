@users
Feature: This feature file will contain all tests related to login

  @logout @remove_user
  Scenario: ID-005
  [Test case to add one single user]
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option
    When I select Users link in dashboard
    Then Add user button should be displayed
    When I click on Add User button
    And I wait 2 seconds
    And For new user I fill username with value "user-ID-005"
    And For new user I fill password with value "Test123$"
    And For new user I fill password confirm with value "Test123$"
    And I save the new user
    Then Add user button should be displayed
    When I search for user with name "user-ID-005"
    Then The number of users displayed should be 1


  @logout @remove_user
  Scenario: ID-006
  [Test case to add multiple users single user]
    Given I login with username "valid_user" and password "valid_password"
    Then I should see logout option
    And I should see change password option
    When I select Users link in dashboard
    Then Add user button should be displayed
    When I create a new user with the following information
      | username     | password |
      | user1-ID-006 | Test123$ |
      | user2-ID-006 | Test123$ |
      | user3-ID-006 | Test123$ |
      | user4-ID-006 | Test123$ |
      | user5-ID-006 | Test123$ |
    When I search for user with name "ID-006"
    And I wait 10 seconds
    Then The number of users displayed should be 5
