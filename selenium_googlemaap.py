from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/maps/@37.5318646,126.8903666,11.23z")
#mainlist = driver.find_element_by_class_name("_2lx2y")
#print(mainlist.text)
#using search bar
search = driver.find_element_by_name("q")
search.send_keys("치과")
#search.send_keys(Keys.RETURN)

find_button = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
find_button.click()


#mainlist = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.xpath, '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/h3/span')))
driver.implicitly_wait(5)
mainlist = driver.find_elements_by_xpath('//*[@class="section-result-title"]')
title = [x.text for x in mainlist]
print(title) #for 
#except:
#	driver.quit()

#mainlist = driver.find_element_by_id("info.search.place.list")

#.quit()
