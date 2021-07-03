from selenium.webdriver.common.by import By
from config.config import swag_labs_base_url
from utils.constants import STANDARD_USER, DEFAULT_STANDARD_PASSWORD, LOCKED_USER


class SwagLabsLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = swag_labs_base_url

    # locators
    username_loc = (By.ID, 'user-name')
    password_loc = (By.ID, 'password')
    login_button_loc = (By.ID, 'login-button')
    locked_out_error_text_loc = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')

    # property

    @property
    def username(self):
        return self.driver.find_element(*self.username_loc)

    @property
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    @property
    def locked_out_error_text(self):
        return self.driver.find_element(*self.locked_out_error_text_loc)

    # method

    def assert_page(self):
        assert self.username
        assert self.password
        assert self.login_button

    def fill_out_creds(self, user_type):
        if user_type == 'standard':
            self.username.send_keys(STANDARD_USER)
        elif user_type == 'locked_out':
            self.username.send_keys(LOCKED_USER)
        self.password.send_keys(DEFAULT_STANDARD_PASSWORD)

    def verify_element_text(self, element):
        assert element.text == 'Epic sadface: Sorry, this user has been locked out.'
