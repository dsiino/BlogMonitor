import time
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=chrome_options)
driver.get("")
assert "Login" in driver.title
btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
btn.click()

elem = driver.find_element_by_name("user")
elem.clear()
elem.send_keys("ABC12345")
driver.find_element_by_name("pass").send_keys("secret-123")

time.sleep(5)

# driver.find_element_by_id("submit").click()
# elem.send_keys(Keys.RETURN)
# assert "bienvenue!" in driver.page_source
driver.close()
