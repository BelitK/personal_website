from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--headless=new")


def login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options) 
    driver.implicitly_wait(5)
    driver.get("https://www.tecnotoys.com.tr/uye-girisi")
    driver.find_element(by=By.NAME, value="email").send_keys('belitberdelk@hotmail.com')
    driver.find_element(by=By.NAME, value="pass").send_keys('O6BfO588')
    driver.find_element(by=By.XPATH, value="//*[@data-selector='login-form-button']").click()

    driver.find_element(by=By.CLASS_NAME, value="user-menu")
    driver.get("https://www.tecnotoys.com.tr/hesabim/siparisler")

    yazan = driver.find_element(by=By.XPATH, value="//td[@class='order-list-status']").text
    driver.quit()
    if yazan == 'Onaylandı':
        return {"status":False}
    return {"status":True}
    
