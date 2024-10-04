from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderTaxi:
    order_a_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')  # Hace clic

    def __init__(self, driver):
        self.driver = driver

    def set_order_a_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.order_a_taxi_button))
        self.driver.find_element(*self.order_a_taxi_button).click()


class FinalizeOrder:
    finalize_taxi_order = (By.CSS_SELECTOR, '.smart-button-wrapper')  # Hace clic
    modal = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_finalize_taxi_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.finalize_taxi_order))
        self.driver.find_element(*self.finalize_taxi_order).click()

    def is_modal_present(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.modal))
        return self.driver.find_element(*self.modal).text
