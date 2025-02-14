Feature: User Authentication

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I enter an invalid email "invalid@example.com"
    And I enter an invalid password "wrongpassword"
    And I click the login button
    Then I should see an error message "Authentication failed."
