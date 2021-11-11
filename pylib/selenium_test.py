import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

UserName = ('samlee')
UserPass = ('Aa0988228843')

driver = webdriver.Firefox(executable_path=r'/run/initramfs/memory/data/HW_test_script/tools/geckodriver')
driver.get("http://eip.efco.com.tw/tw/index.htm?lang=tw")
time.sleep(5)

#elem = driver.find_element_by_xpath("//frame[@name='txtAccount']").send_keys("samlee")
#elem = driver.find_element_by_xpath('//frame[@name="loginFrameData"]')
#driver.switch_to.frame(frame)
#elem = driver.find_element_by_xpath("//*[@type="text" and @name="txtAccount"]")
#elem = driver.find_element(By.XPATH, //table[@class="righttable_bg"]/tbody/tr/td/table/tbody/tr/td/input.chgtable02)
#elem = driver.find_element(By.XPATH, "//input[contains(@name,'txtAccount']")
elem = driver.find_element(By.XPATH, '//*[@class="chgtable02" and @name=" txtAccount"]')

#elem = driver.find_element_by_xpath('/html/frameset/frame#loginPage/html/body/form/table/tbody/tr/td/table.righttable_bg/tbody/tr/td/table/tbody/tr/td/input.chgtable02/txtAccount')
#elem = driver.find_element_by_name("*txtAccount*")
print(elem)
elem.clear()
elem.send_keys("samlee")

elem2 = driver.find_element_by_xpath("//cla[@name='txtPassword']")
elem2.clear()
elem2.send_keys("Aa0988228843")
elem2.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.title)
print(driver.page_source)

#time.sleep(5)
driver.close()