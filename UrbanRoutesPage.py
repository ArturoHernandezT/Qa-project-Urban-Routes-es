from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import methods


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

    order_a_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')  # Hace clic

    def set_order_a_taxi_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.order_a_taxi_button))
        self.driver.find_element(*self.order_a_taxi_button).click()

    finalize_taxi_order = (By.CSS_SELECTOR, '.smart-button-wrapper')  # Hace clic
    modal = (By.CSS_SELECTOR, '.order-header-title')

    def set_finalize_taxi_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.finalize_taxi_order))
        self.driver.find_element(*self.finalize_taxi_order).click()

    def is_modal_present(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.modal))
        return self.driver.find_element(*self.modal).text

    select_comfort_rate = (By.XPATH, "//*[@class='tcard-title' and text()='Comfort']")  # Hace clic
    phone_number_placeholder = (By.CSS_SELECTOR, '.np-button')  # Hace clic
    phone_number_input = (By.ID, 'phone')  # Envia datos
    next_button = (By.CSS_SELECTOR, '.button.full')  # Hace clic
    sms_code_input = (By.XPATH, "//div[@class='input-container']/input[@id='code' and @class='input']")  # Envia datos
    submit_button = (By.XPATH, '//div[@class="buttons"]/button[text()="Confirmar"]')  # Hace clic
    reqs_body = (By.XPATH, '//div[text()="Manta y pañuelos"]')
    req_header = (By.CSS_SELECTOR, '.reqs-header')
    phone_field = (By.CLASS_NAME, 'np-text')

    def set_select_comfort_rate(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(self.select_comfort_rate))
        self.driver.find_element(*self.select_comfort_rate).click()

    def set_reqs_body(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.req_header))
        return self.driver.find_element(*self.reqs_body).text

    def set_phone_number_placeholder(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.phone_number_placeholder))
        self.driver.find_element(*self.phone_number_placeholder).click()

    def set_phone_number_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.phone_number_input))
        numero = data.phone_number
        self.driver.find_element(*self.phone_number_input).send_keys(numero)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).text

    def set_next_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def set_sms_code_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.sms_code_input))
        code = methods.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.sms_code_input).send_keys(code)

    def set_submit_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//div[@class="buttons"]/button[text()="Confirmar"]')))
        self.driver.find_element(*self.submit_button).click()

    payment_method = (By.CSS_SELECTOR, '.pp-button')  # Hace clic
    add_credit_card = (By.CSS_SELECTOR, '.pp-plus-container')  # Hace clic
    credit_card_number_input = (By.ID, 'number')  # Envia datos
    credit_card_code_input = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')  # Envia datos
    focus_change = (By.CSS_SELECTOR, '.card-wrapper')  # Hace clic
    add_filled_credit_card = (By.XPATH, '//button[text()="Agregar"]')  # Hace clic
    close_button_payment_method = (By.XPATH, "//div[@class='payment-picker open']//div[@class='overlay']/following-sibling::div[@class='modal']"
              "//div[@class='section active']//button[@class='close-button section-close']")  # Hace clic
    check_credit_card = (By.XPATH, '//*[@id="card-1"]')

    def set_paymen_method(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.payment_method))
        self.driver.find_element(*self.payment_method).click()

    def set_add_credit_card(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.add_credit_card))
        self.driver.find_element(*self.add_credit_card).click()

    def set_credit_card_number_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.credit_card_number_input))
        numero_tarjeta = data.card_number
        self.driver.find_element(*self.credit_card_number_input).send_keys(numero_tarjeta)

    def get_credit_card(self):
        return self.driver.find_element(*self.credit_card_number_input).get_property('value')

    def set_credit_card_code_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.credit_card_code_input))
        codigo_tarjeta = data.card_code
        self.driver.find_element(*self.credit_card_code_input).send_keys(codigo_tarjeta)

    def get_credit_card_code(self):
        return self.driver.find_element(*self.credit_card_code_input).get_property('value')

    def set_focus_change(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.focus_change))
        self.driver.find_element(*self.focus_change).click()

    def set_add_filled_credit_card(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.add_filled_credit_card))
        self.driver.find_element(*self.add_filled_credit_card).click()

    def get_check_add_credit_card(self):
        return self.driver.find_element(By.XPATH, '//*[@id="card-1"]').get_property('name')

    def set_close_button_payment_method(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.close_button_payment_method))
        self.driver.find_element(*self.close_button_payment_method).click()

    message_to_the_driver = (By.XPATH, '//*[@id="comment"]')  # Envia datos
    blankets = (By.XPATH, "//div[text()='Manta y pañuelos']/following-sibling::div//span[@class='slider round']")  # Hace clic
    order_2_icecream = (By.XPATH, "//div[text()='Helado']/following-sibling::div[@class='r-counter']//div[@class='counter-plus']")  # Hace clic
    ice_cream_counter = (By.XPATH, "//div[text()='Helado']/following-sibling::div[@class='r-counter']//div[@class='counter-value']")

    def set_message_to_the_driver(self):
        mensaje = data.message_for_driver
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.message_to_the_driver))
        self.driver.find_element(*self.message_to_the_driver).send_keys(mensaje)

    def get_message(self):
        return self.driver.find_element(*self.message_to_the_driver).get_attribute('value')

    def set_blankets(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.blankets))
        self.driver.find_element(*self.blankets).click()

    def check_blankets(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.blankets))
        return self.driver.find_element(*self.blankets).is_selected()

    def set_order_2_icecream(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_2_icecream))
        ice_cream = self.driver.find_element(*self.order_2_icecream)
        for n in range(2):
            ice_cream.click()

    def is_2_icecream_selected(self):
        return self.driver.find_element(*self.ice_cream_counter).text
