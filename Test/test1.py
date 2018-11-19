from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/cramirez.CAFETO/PycharmProjects/untitled/drivers/chromedriver.exe")
# driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("   ")
driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.VlcLAe > center > input[type='submit' ]:nth-child(1)").send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
