import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
if __name__ == "__main__":
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("window-size=1080,800")
    #options.add_argument('window-size=800x600')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    wait = WebDriverWait(driver, 1000)
    with open("___1_18_2_newmods.txt", "r") as f:
        for i, line in enumerate(f):
            if i != 0:
                continue
            line = line.replace("www", "beta")[:-1] + "/files"
            print(line)
            driver.get(line)
            el = driver.find_element(By.CLASS_NAME, "filters")
            versions = el.find_elements(By.CLASS_NAME, "select-dropdown")
            versions[0].click()
            wait.until(EC.element_to_be_clickable(versions[0].find_element(By.XPATH, ".//li[text()='1.18.2']"))).click()
            #time.sleep(0.1)
            #versions[0].find_element(By.XPATH, ".//li[text()='1.18.2']").click()
            #time.sleep(1)
            wait.until(EC.element_to_be_clickable(versions[1])).click()
            #time.sleep(0.1)
            wait.until(EC.element_to_be_clickable(versions[1].find_element(By.XPATH, ".//li[text()='Forge']"))).click()
            file = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "file-row")))
            #btn1 = file.find_element(By.CLASS_NAME, "btn-more-options")
            #aaa = driver.find_elements(By.XPATH, "//div[@class='file-row'][1]/div/div/ul[@id='contextMenu']/li/a")
            #print(aaa[0].text)
            #print(aaa[1].text)
            #quit()
            print(file.find_element(By.XPATH, ".//div/div/button").text)
            #while True:
            #    try:
            wait.until(EC.element_to_be_clickable(file.find_element(By.XPATH, ".//button"))).click()
            #        break
            #    except:
            #        pass
            #wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "btn-more-options"))).click()
            time.sleep(100000)

            #files = driver.find_element(By.CLASS_NAME, "files-cards-list").find_elements(By.CLASS_NAME, "file-card")
            #files[0].click()
            #soup = BeautifulSoup(response.text, 'html.parser')
            #driver.get(line)
            #time.sleep(15)
            #quit()

