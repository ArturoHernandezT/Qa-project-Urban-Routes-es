import data
from selenium import webdriver
from home import UrbanRoutesPage
from params_select import ComfortRate
from params_select import PaymenthMethod
from params_select import AdditionalItems
from order_taxi import OrderTaxi, FinalizeOrder


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
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

    def test_order_a_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        click_order_taxi = OrderTaxi(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        click_order_taxi.set_order_a_taxi_button()

    def test_fill_phone_and_code(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        click_order_taxi = OrderTaxi(self.driver)
        select_comfort = ComfortRate(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        click_order_taxi.set_order_a_taxi_button()
        select_comfort.set_select_comfort_rate()
        assert select_comfort.get_comfort() == 'Comfort'
        select_comfort.set_phone_number_placeholder()
        select_comfort.set_phone_number_input()
        assert select_comfort.get_phone() == data.phone_number
        select_comfort.set_next_button()
        select_comfort.set_sms_code_input()
        select_comfort.set_submit_button()

    def test_payment_method(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        click_order_taxi = OrderTaxi(self.driver)
        select_comfort = ComfortRate(self.driver)
        payment_method = PaymenthMethod(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        click_order_taxi.set_order_a_taxi_button()
        select_comfort.set_select_comfort_rate()
        select_comfort.set_phone_number_placeholder()
        select_comfort.set_phone_number_input()
        select_comfort.set_next_button()
        select_comfort.set_sms_code_input()
        select_comfort.set_submit_button()
        payment_method.set_paymen_method()
        payment_method.set_add_credit_card()
        payment_method.set_credit_card_number_input()
        assert payment_method.get_credit_card() == data.card_number
        payment_method.set_credit_card_code_input()
        assert payment_method.get_credit_card_code() == data.card_code
        payment_method.set_focus_change()
        payment_method.set_add_filled_credit_card()
        assert payment_method.get_check_add_credit_card() == 'card-1'
        payment_method.set_close_button_payment_method()

    def test_additional_items(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        click_order_taxi = OrderTaxi(self.driver)
        select_comfort = ComfortRate(self.driver)
        additional_items = AdditionalItems(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        click_order_taxi.set_order_a_taxi_button()
        select_comfort.set_select_comfort_rate()
        additional_items.set_message_to_the_driver()
        assert additional_items.get_message() == data.message_for_driver
        additional_items.set_blankets()
        additional_items.set_order_2_icecream()
        assert additional_items.is_2_icecream_selected() == '2'

    def test_finalize_order(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        click_order_taxi = OrderTaxi(self.driver)
        select_comfort = ComfortRate(self.driver)
        finalize_order = FinalizeOrder(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        click_order_taxi.set_order_a_taxi_button()
        select_comfort.set_select_comfort_rate()
        finalize_order.set_finalize_taxi_order()
        assert finalize_order.is_modal_present() == 'Buscar automóvil'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
