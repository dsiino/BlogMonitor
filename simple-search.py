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
elem.send_keys("asd")
driver.find_element_by_name("pass").send_keys("123")

time.sleep(1)

elem.send_keys(Keys.RETURN)
driver.find_element_by_id("forum-pill").click()
# stars = driver.find_elements(By.XPATH, "//tbody[@id='forum-body']/tr/td/i")
stars = driver.find_elements_by_xpath("//tbody[@id='forum-body']/tr/td/i//preceding-sibling::*")
# stars = driver.find_elements(By.XPATH, "//tbody[@id='forum-body']/tr/td/a[@onclick='invalidate_forum_cache()']")
print(stars.__len__())
# astar = driver.find_element(By.XPATH, "//tbody[@id='forum-body']/tr/td/i/preceding-sibling::a")
# print(astar.text)
# astar.click()

for star in stars:
    #     anchor = star.find_element_by_xpath(".//../a")
    print(star.text)
    star.click()
# fa fa-star pull-right text-danger
# assert "Forum" in driver.page_source
# driver.close()
