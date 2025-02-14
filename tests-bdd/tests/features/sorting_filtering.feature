Feature: Sorting and Filtering

  Scenario: Sort items by price from low to high
    Given I am on the shop page
    When I sort items by "Price: Lowest first"
    Then I should see items sorted by price

  Scenario: Filter items by category "Dresses"
    Given I am on the shop page
    When I filter items by category "Dresses"
    Then I should see only dresses
