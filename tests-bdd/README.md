# BDD Test Scenarios for Automation Practice

This project contains **BDD (Behavior-Driven Development) test scenarios** for an e-commerce website using `pytest-bdd` and `selenium`. The following features are covered:

## Features

### 1. User Authentication

- **Login with invalid credentials**
  - Given I am on the login page
  - When I enter an invalid email `invalid@example.com`
  - And I enter an invalid password `wrongpassword`
  - And I click the login button
  - Then I should see an error message `Authentication failed.`

### 2. User Registration

- **Successful registration with valid data**

  - Given I am on the registration page
  - When I enter a valid email `testuser@example.com`
  - And I fill in the registration form with valid details
  - And I submit the form
  - Then I should see a confirmation message `Your account has been created.`

- **Registration with missing required fields**
  - Given I am on the registration page
  - When I enter a valid email `testuser@example.com`
  - And I submit the form without filling required fields
  - Then I should see error messages for the missing fields

### 3. Shopping Flow

- **Attempt to add an unavailable item to the cart and verify the cart is empty**
  - Given I am on the home page
  - When I search for an item `Dress`
  - And I attempt to add the first item to the cart
  - Then I should see an out-of-stock alert
  - When I go to the cart page
  - Then my cart should be empty

### 4. Sorting and Filtering

- **Sort items by price from low to high**

  - Given I am on the shop page
  - When I sort items by `Price: Lowest first`
  - Then I should see items sorted by price

- **Filter items by category "Dresses"**
  - Given I am on the shop page
  - When I filter items by category `Dresses`
  - Then I should see only dresses

## Prerequisites

- Ensure you have `Python 3.10+` installed.
- Install dependencies using the provided script.

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/HLyczak/frontend-bdd
   cd tests-bdd
   ```
2. Run the installation script:

   ```sh
   ./install.sh
   ```

   ```sh
   source .venv/bin/activate
   ```

## Running Tests

To execute all tests, use the following command:

```sh
pytest tests/ --html=report.html --self-contained-html
```

If you want to run a specific test suite, for example, **login tests**, use:

```sh
pytest tests/steps/test_login.py --html=report.html --self-contained-html
```

## Viewing the Test Report

After running the tests, a **colorful HTML report** will be generated in the project directory as `report.html`.
To open the report in a browser, use:

```sh
open report.html  # macOS
start report.html  # Windows
xdg-open report.html  # Linux
```

### Example Report Output

The generated `report.html` will contain:

- ✅ Passed and ❌ Failed tests clearly highlighted
- Execution time for each test
- Detailed logs for debugging failures

## Notes

- The **registration feature** is a prerequisite for login testing, ensuring that a user is created before attempting to log in.
- These scenarios are **example test cases** and can be extended based on application behavior.
