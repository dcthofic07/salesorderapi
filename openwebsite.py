from selenium import webdriver
import time
import opensite.getdatafromxml


class OpenWebsite():

    def a_test(self):
        driver = webdriver.Firefox()
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
        login_id.send_keys(opensite.getdatafromxml.test2.b_test())
        time.sleep(10)
        driver.quit()


test1 = OpenWebsite()
test1.a_test()
