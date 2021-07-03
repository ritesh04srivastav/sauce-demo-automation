@ritesh
Feature: Tests to verify swag lab login page

  Background:
    Given I have a swag labs account
    And I load the swag_labs_login_page

  Scenario: User can login with valid creds
    When I fill out the standard credentials on the swag_labs_login_page
    And I click the login_button on the swag_labs_login_page
    Then I see the swag_labs_products_page

  Scenario: Validate error if user tries to login with locked out creds
    When I fill out the locked_out credentials on the swag_labs_login_page
    And I click the login_button on the swag_labs_login_page
    Then I see the locked_out_error_text on the swag_labs_login_page
