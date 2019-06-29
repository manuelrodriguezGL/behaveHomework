@users
  Feature: This suite will contain all the tests related to folder management

    @folders.create_successful
    Scenario: 001
      [This test case adds a new folder]
      Given I login with username "admin" and password "admin"
      Then I should see logout option
      And I should see change password option
      When I click on Folders option on Users dashboard
      Then The folder management page loads
      When I create a new folder and click Save button
      | folder_name   |
      | test_folder_1 |
      Then The folder name "test_folder_1" appears on Folders table