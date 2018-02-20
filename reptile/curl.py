from selenium import webdriver
import time
 
driver = webdriver.Ie()
driver.get("http://jiedada.top:8080/location/")
print(driver.page_source)
driver.close()