Feature: Tests to verify swag lab login pageghg

  Background: xvbdf
    Given I have a swag labs account

  Scenario: User can login with valids credsgh
    Given I load the swag_labs_login_page
    When I fill out the standard credentials on the swag_labs_login_page
    And I click the login_button on the swag_labs_login_page
    Then I see the swag_labs_products_page
