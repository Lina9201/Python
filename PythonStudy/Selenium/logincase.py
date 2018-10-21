from selenium import webdriver

url = "http://www.hordehome.com"
driver = webdriver.Chrome()
driver.get(url)

#隐式等待10s
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='main']/div/div/header/div/div/div[2]/span/button[2]").click()

driver.find_element_by_id("login-account-name").send_keys("Lina")
driver.find_element_by_id("login-account-password").send_keys("!QAZ2wsx")
driver.find_element_by_css_selector(".btn.btn-large.btn-primary").click()

t = driver.find_element_by_id("current-user").get_attribute("title")


print(t)

if t == "Lina":
    print("Login Successfully!")
else:
    print("Login failed!")

driver.quit()
