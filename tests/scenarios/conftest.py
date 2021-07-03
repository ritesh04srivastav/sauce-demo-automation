import pytest
from pytest_bdd import given, parsers, when, then
from selenium import webdriver
from lib.page_object_models.swag_labs_login_page import SwagLabsLoginPage
from lib.page_object_models.swag_labs_products_page import SwagLabsProductsPage
from utils.constants import CHROME_PATH


@pytest.fixture
def page_objects():
    """Dictionary to hold page objects"""
    return {}


@pytest.fixture
def driver():
    """initiates browser driver and quits at the end of the tests"""
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()

@given('I have a swag labs account')
def swag_labs_account(page_objects, driver):
    page_objects['swag_labs_login_page'] = SwagLabsLoginPage(driver)
    page_objects['swag_labs_products_page'] = SwagLabsProductsPage(driver)


@given(parsers.parse('I load the {page_name:w}'))
def load_given(page_objects, driver, page_name):
    driver.get(page_objects[page_name].url)
    page_objects[page_name].assert_page()


@when(parsers.parse('I fill out the {user_type:w} credentials on the {page_name:w}'))
def fill_out_creds(page_objects, user_type, page_name):
    page_objects[page_name].fill_out_creds(user_type)


@when(parsers.parse('I click the {element_name:w} on the {page_name:w}'))
def click_element(page_objects, element_name, page_name):
    page = page_objects.get(page_name)
    element = getattr(page, element_name)
    element.click()


@then(parsers.parse('I see the {page_name:w}'))
def see_page(page_objects, page_name):
    page_objects[page_name].assert_page()


@then(parsers.parse('I see the {element_name} on the {page_name:w}'))
def see_element(page_objects, element_name, page_name):
    page = page_objects.get(page_name)
    element = getattr(page, element_name)
    page.verify_element_text(element)

