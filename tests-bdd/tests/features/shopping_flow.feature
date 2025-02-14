Feature: Shopping Flow

  Scenario: Attempt to add an unavailable item to the cart and verify the cart is empty
    Given I am on the home page
    When I search for an item "Dress"
    And I attempt to add the first item to the cart
    Then I should see an out-of-stock alert
    When I go to the cart page
    Then my cart should be empty
