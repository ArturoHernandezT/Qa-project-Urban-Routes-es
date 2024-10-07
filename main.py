from selenium import webdriver
from UrbanRoutesPage import *


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.set_order_a_taxi_button()

    def test_comfort_rate(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        assert "Manta y pañuelos" in routes_page.set_reqs_body(), 'No se ha seleccionado la tarifa Comfort'

    def test_fill_phone_and_code(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_phone_number_placeholder()
        routes_page.set_phone_number_input()
        routes_page.set_next_button()
        routes_page.set_sms_code_input()
        routes_page.set_submit_button()
        assert routes_page.get_phone() == data.phone_number, 'No se ha introducido el numero correctamente'

    def test_payment_method(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_phone_number_placeholder()
        routes_page.set_phone_number_input()
        routes_page.set_next_button()
        routes_page.set_sms_code_input()
        routes_page.set_submit_button()
        routes_page.set_paymen_method()
        routes_page.set_add_credit_card()
        routes_page.set_credit_card_number_input()
        assert routes_page.get_credit_card() == data.card_number
        routes_page.set_credit_card_code_input()
        assert routes_page.get_credit_card_code() == data.card_code
        routes_page.set_focus_change()
        routes_page.set_add_filled_credit_card()
        assert routes_page.get_check_add_credit_card() == 'card-1'
        routes_page.set_close_button_payment_method()

    def test_message_to_the_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_message_to_the_driver()
        assert routes_page.get_message() == data.message_for_driver

    def test_order_blankets(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_blankets()
        assert routes_page.check_blankets() == True, 'No se ha seleccionado correctamente el checkbox'

    def test_order_2_icecream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_order_2_icecream()
        assert routes_page.is_2_icecream_selected() == '2'

    def test_taxi_modal_is_displayed(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.set_order_a_taxi_button()
        routes_page.set_select_comfort_rate()
        routes_page.set_finalize_taxi_order()
        assert routes_page.is_modal_present() == 'Buscar automóvil'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
