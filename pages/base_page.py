from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DRIVER_NAME


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # def close_cookie_modal(self):
    #     self.wait_element_to_be_clickable(self.driver, (By.XPATH, BasePageLocators.close_cookies_modal_button)).click()
    #     time.sleep(2)

    def click_on_the_element(self, xpath):
        self.scroll_to_element(self.driver, xpath)
        self.wait_element_to_be_clickable(self.driver, (By.XPATH, xpath))
        self.driver.find_element(By.XPATH, xpath).click()

    # def switch_to_tab_with_url(self, driver, expected_url, timeout=5):
    #     WebDriverWait(driver, timeout).until(expected_conditions.number_of_windows_to_be(2))
    #     all_windows = driver.window_handles
    #     current_window = driver.current_window_handle
    #
    #     for window in all_windows:
    #         if window != current_window:
    #             driver.switch_to.window(window)
    #             WebDriverWait(driver, timeout).until(expected_conditions.url_contains(expected_url))
    #         else:
    #             driver.switch_to.window(current_window)

    def wait_element_to_be_clickable(self, driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_element_to_be_visible(self, driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_element_not_visible(self, driver, locator, timeout=10):
        try:
            # проверяем, существует ли элемент на странице
            element = driver.find_element(*locator)
            WebDriverWait(driver, timeout).until_not(expected_conditions.visibility_of(element))
            return True
        except NoSuchElementException:
            return True  # если элемент не найден
        except TimeoutException:
            return False  # элемент существует, но не стал невидимым за отведённое время

    def scroll_to_element(self, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_element_to_be_visible(driver, (By.XPATH, xpath))

    #только для хрома
    def drag_and_drop_element(self, element_from, element_to, driver):
        from_element = self.wait_element_to_be_visible(driver, element_from)
        to_element = self.wait_element_to_be_visible(driver, element_to)

        if driver.name == 'chrome':
            ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

        # Используем JavaScript для выполнения drag-and-drop в браузере Firefox
        else:
            driver.execute_script("""
                    var fromElement = arguments[0];
                    var toElement = arguments[1];

                    // Получаем координаты элементов
                    var rectFrom = fromElement.getBoundingClientRect();
                    var rectTo = toElement.getBoundingClientRect();

                    // Создаем событие mousedown для начала перетаскивания
                    var dragStartEvent = new MouseEvent('mousedown', { 
                        bubbles: true, 
                        cancelable: true, 
                        clientX: rectFrom.left + (rectFrom.width / 2), 
                        clientY: rectFrom.top + (rectFrom.height / 2)
                    });
                    fromElement.dispatchEvent(dragStartEvent);

                    // Перемещаем элемент к новому месту
                    var mouseMoveEvent = new MouseEvent('mousemove', {
                        bubbles: true,
                        cancelable: true,
                        clientX: rectTo.left + (rectTo.width / 2),
                        clientY: rectTo.top + (rectTo.height / 2)
                    });
                    fromElement.dispatchEvent(mouseMoveEvent);

                    // Отпускаем кнопку мыши на целевом элементе
                    var dropEvent = new MouseEvent('mouseup', { 
                        bubbles: true, 
                        cancelable: true, 
                        clientX: rectTo.left + (rectTo.width / 2), 
                        clientY: rectTo.top + (rectTo.height / 2)
                    });
                    toElement.dispatchEvent(dropEvent);
                """, from_element, to_element)