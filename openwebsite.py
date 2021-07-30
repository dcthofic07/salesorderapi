from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time
import getdatafromxml
import unittest


class TestOpenWebsite(unittest.TestCase):

    def test_a(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=opts)
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollBy(0, 900);")
        time.sleep(3)
        driver.switch_to.frame("courses-iframe")
        time.sleep(2)
        link = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/nav/div/div[2]/div/div/a")
        time.sleep(5)
        link.click()
        time.sleep(5)
        login_id = driver.find_element_by_xpath("//*[@id='email']")
        self.assertEqual(True, login_id.is_enabled(), "element not found")
        login_id.send_keys(getdatafromxml.TestMatchSalesOrder.test_b(self))
        time.sleep(10)
        self.screen_shot(driver)
        driver.quit()

    def screen_shot(self, driver):
        filename = str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "screenshot"
        destination_file = screenshot_directory + filename
        try:
            driver.save_screenshot(destination_file)
            print("Screen shot saved to directory " + destination_file)
            driver.quit()
        except NotADirectoryError:
            print("Not a directory error")



if __name__ == "__main__":
    unittest.main(verbosity=2)
