from webdriverChrome import WebDriver
class Bot:
    def __init__(self, start_page_url):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def refresh(self):
        self.webdriver.refresh()

    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def select_item(self, item_name):
        item = self.webdriver.find_element_by_visible_text(item_name)
        return self.webdriver.click_on_element(item)

    def select_colorway(self, item_colorway_position):
        colorway_box_x_path = '//*[contains(@class, "styles ")]/li[{}]'.format(
            item_colorway_position)
        colorway_box = self.webdriver.find_element_by_x_path(
            colorway_box_x_path)
        return self.webdriver.click_on_element(colorway_box)

    def select_size(self, item_size):
        return self.webdriver.select_dropdown_option('//*[@name="s"]', item_size)

    def add_to_cart(self):
        add_to_cart_button = self.webdriver.find_element_by_x_path("//input[@type='submit']")
        return self.webdriver.click_on_element(add_to_cart_button)

    def go_to_checkout(self):
        checkout_button = self.webdriver.find_element_by_x_path('//a[@class="button checkout"]')
        return self.webdriver.click_on_element(checkout_button)

    def fill_in_checkout_form(self, billing_info):
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="name"]', billing_info["fullName"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="email"]', billing_info["email"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="tel"]', billing_info["phone"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="address"]', billing_info["address"]
        )
        #if billing_info["unit"]:
            #self.webdriver.fill_in_input_field(
            #    '//input[@placeholder="apt, unit, etc"]', billing_info["unit"]
            #)Causes a glitch with city address
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="zip"]', billing_info["zip"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="city"]', billing_info["city"]
        )
        self.webdriver.select_dropdown_option(
            '//*[@id="order_billing_state"]', billing_info["state"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="number"]', billing_info["ccNumber"]
        )
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_month"]', billing_info["expM"])
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_year"]', billing_info["expY"])
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="CVV"]', billing_info["cvv"])


    def agree_to_terms(self):
        terms_checkbox = self.webdriver.find_element_by_x_path(
            "(//div[@class='icheckbox_minimal'])[position()=2]")
        return self.webdriver.click_on_element(terms_checkbox)

    def process_payment(self):
        process_payment_button = self.webdriver.find_element_by_x_path("//input[@type='submit' and @name='commit']")
        return self.webdriver.click_on_element(process_payment_button)
