Feature: User Registration

  Scenario: Successful registration with valid data
    Given I am on the registration page
    When I enter a valid email testuser@example.com
    And I fill in the registration form with valid details
    And I submit the form
    Then I should see a confirmation message Your account has been created.


  Scenario: Registration with missing required fields
    Given I am on the registration page
    When I enter a valid email testuser@example.com
    And I submit the form without filling required fields
    Then I should see error messages for the missing fields