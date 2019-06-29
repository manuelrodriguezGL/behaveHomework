@users
Feature: This suite will contain all the tests related to folder management

  @folders.create_successful @logout
  Scenario:
  [This test case adds a new folder]
    Given I login with username "admin" and password "admin"
    Then I should see logout option
    And I should see change password option
    When I click on Folders option on Users dashboard
    Then The folder management page loads
    When I create a new folder and click Save button
      | folder_name     |
      | test_folder_001 |
    Then The folder name "test_folder_001" appears on Folders table
    And I logout the application


  @folders.remove_successful @duplicate
  Scenario: 002
  [This test case removes a new folder using API]
    Given I login with username "admin" and password "admin"
    Then I should see logout option
    And I should see change password option
    When I click on Folders option on Users dashboard
    Then The folder management page loads
    When I create a new folder and click Save button
      | folder_name     |
      | test_folder_002 |
    Then The folder name "test_folder_002" appears on Folders table
    And I logout the application


  @folders.remove_successful_ui @logout
  Scenario: 003
  [This test case removes a new folder]
    Given I login with username "admin" and password "admin"
    Then I should see logout option
    And I should see change password option
    When I click on Folders option on Users dashboard
    Then The folder management page loads
    And The folder name "test_folder_003" appears on Folders table
    Then I click on Remove button for "test_folder_003"
    And I confirm folder deletion
    Then The folder name "test_folder_003" is not on Folders table anymore
    And I logout the application