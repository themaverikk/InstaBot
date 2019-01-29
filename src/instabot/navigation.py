from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def scroll_element(driver, element):
    y = element.location['y']

    scroll_nav_out_of_way = 'window.scrollBy(0, {});'.format(y)
    driver.execute_script(scroll_nav_out_of_way)


def hide_notification_popup(driver):
    WebDriverWait(driver, 60).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.aOOlW.HoLwm')))

    driver.find_element_by_css_selector('.aOOlW.HoLwm').click()
