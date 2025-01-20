from time import sleep

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BasePageData
from helpers import generate_register_data
from xpath_data import HomePagePaths, LoginPagePaths, RegistrationPagePaths


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_the_element(self, driver, xpath):
        # прокрутка к элементу и ожидание, что он станет кликабельным
        self.wait_element_to_be_clickable(driver, xpath)
        self.scroll_to_element(driver, xpath)

        modals = [
            HomePagePaths.extra_modal_1,
            HomePagePaths.extra_modal_2
        ]

        for modal_xpath in modals:
            # Найти модальное окно, если оно есть
            modal_elements = driver.find_elements(By.XPATH, modal_xpath)
            if modal_elements:
                # Если найдено, скрыть его
                driver.execute_script("arguments[0].style.display = 'none';", modal_elements[0])

        self.driver.find_element(By.XPATH, xpath).click()

    def fill_the_field(self, driver, xpath, value):
        self.scroll_to_element(driver, xpath)
        self.wait_element_to_be_clickable(driver, xpath).send_keys(value)

    def wait_element_to_be_clickable(self, driver, xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    def wait_element_to_be_visible(self, driver, xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def wait_element_not_visible(self, driver, xpath, timeout=10):
        try:
            # проверяем, существует ли элемент на странице
            WebDriverWait(driver, timeout).until_not(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except NoSuchElementException:
            return True  # если элемент не найден
        except TimeoutException:
            return False  # элемент существует, но не стал невидимым за отведённое время

    def scroll_to_element(self, driver, xpath):
        sleep(1)
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_element_to_be_visible(driver, xpath)

    def drag_and_drop_element(self, element_from_xpath, element_to_xpath, driver):
        self.scroll_to_element(driver, element_from_xpath)
        from_element = self.wait_element_to_be_visible(driver, element_from_xpath)
        to_element = self.wait_element_to_be_visible(driver, element_to_xpath)

        if driver.name == 'chrome':
            ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

        else:
            script = """
                    function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                        var dataTransfer = new DataTransfer();
                        var dragStartEvent = new DragEvent('dragstart', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragStartEvent);
                        var dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        destinationNode.dispatchEvent(dropEvent);
                        var dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragEndEvent);
                    }
                    simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                    """
            self.driver.execute_script(script, from_element, to_element)

    def login(self, driver):

        register_data = generate_register_data()

        driver.get(BasePageData.REGISTER_PAGE_URL)

        self.fill_the_field(driver, RegistrationPagePaths.rp_name_input, register_data["name"])
        self.fill_the_field(driver, RegistrationPagePaths.rp_email_input, register_data["login"])
        self.fill_the_field(driver, RegistrationPagePaths.rp_password_input, register_data["password"])
        self.click_on_the_element(driver, RegistrationPagePaths.sign_up_button)

        driver.get(BasePageData.LOGIN_PAGE_URL)

        self.fill_the_field(driver, LoginPagePaths.lp_email_input, register_data["login"])
        self.fill_the_field(driver, LoginPagePaths.lp_password_input, register_data["password"])
        self.click_on_the_element(driver, LoginPagePaths.login_button)

        self.wait_element_to_be_visible(driver, HomePagePaths.collect_a_burger_header)
