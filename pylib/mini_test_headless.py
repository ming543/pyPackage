
import time, os
from showbox import showbox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

#Start the firefox
driver = webdriver.Firefox(firefox_options=fireFoxOptions, executable_path=r'/run/initramfs/memory/data/HW_test_script/tools/geckodriver')
#driver.get("http://10.0.0.100")
driver.get("http://httpbin.org/user-agent")
print(driver.page_source)
driver.close

#485 Check box
showbox().textbox('Please link loopback cable of 485')

#Test of RS485
Select(driver.find_element_by_id("SerialModeSelect")).select_by_value('485')
#click for start test
driver.find_element_by_id("SerialCmdButton").click()
time.sleep(10)
#click for stop test
driver.find_element_by_id("SerialCmdButton").click()
print(driver)

#f = open('/run/initramfs/memory/data/HW_test_script/tmp/mini_test.log', 'w')
#f.write(log.encode('utf-8'))
#print(driver.f)
#f.close


#Select(driver.find_element_by_id("SerialModeSelect")).select_by_value('232')
#mini_232_test = driver.find_element_by_id("SerialCmdButton").send_keys(Keys.RETURN)




#time.sleep(5)
driver.close()
