from time import sleep

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import HomePagePaths


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_the_element(self, xpath):
        # прокрутка к элементу и ожидание, что он станет кликабельным
        self.wait_element_to_be_clickable(xpath)
        self.scroll_to_element(xpath)

        modals = [
            HomePagePaths.extra_modal_1,
            HomePagePaths.extra_modal_2
        ]

        for modal_xpath in modals:
            # Найти модальное окно, если оно есть
            modal_elements = self.driver.find_elements(By.XPATH, modal_xpath)
            if modal_elements:
                # Если найдено, скрыть его
                self.driver.execute_script("arguments[0].style.display = 'none';", modal_elements[0])

        self.driver.find_element(By.XPATH, xpath).click()

    def fill_the_field(self, xpath, value):
        self.scroll_to_element(xpath)
        self.wait_element_to_be_clickable(xpath).send_keys(value)

    def wait_element_to_be_clickable(self, xpath, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    def wait_element_to_be_visible(self, xpath, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def wait_element_not_visible(self, xpath, timeout=10):
        try:
            # проверяем, существует ли элемент на странице
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except NoSuchElementException:
            return True  # если элемент не найден
        except TimeoutException:
            return False  # элемент существует, но не стал невидимым за отведённое время

    def scroll_to_element(self, xpath):
        sleep(1)
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_element_to_be_visible(xpath)

    def drag_and_drop_element(self, element_from_xpath, element_to_xpath):
        self.scroll_to_element(element_from_xpath)
        from_element = self.wait_element_to_be_visible(element_from_xpath)
        to_element = self.wait_element_to_be_visible(element_to_xpath)

        if self.driver.name == 'chrome':
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
