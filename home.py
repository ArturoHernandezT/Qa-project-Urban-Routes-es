from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')  #Envia datos
    to_field = (By.ID, 'to')  #Envia datos

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            self.from_field))  # SE TIENE QUE AGREGAR UNA ESPERA EXPLÍCITA
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')
