from selenium import webdriver
#options = webdriver.FirefoxOptions()
#options.set_headless()
#options.add_argument('--disable-gpu')
#driver = webdriver.Firefox(firefox_options=options)
driver = webdriver.Firefox()
driver.get('http://httpbin.org/user-agent')
print(driver.page_source)
driver.close()


