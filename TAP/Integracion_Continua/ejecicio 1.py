import random
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')

def dormir():
    return sleep(random.uniform(2,4))


driver.get('http://greenway.greensqa.com/TP2/Ejercicios/Basico/Ejercicio-1.html')
driver.maximize_window()
dormir()
boton = driver.find_element_by_xpath('//i[@class="material-icons"]')
dormir()
boton.click()

dormir()

page_dos = driver.find_element_by_xpath('//*[text()="2"]')
page_dos.click()

dormir()

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@scrolling="no"]'))
dormir()
texto = driver.find_element_by_xpath('//input[@id="last_name"]')
dormir()
texto.click()
dormir()
texto.send_keys("ferrari")

driver.switch_to.default_content()

boton2 = driver.find_element_by_xpath('//i[@class="material-icons"]')
dormir()
boton2.click()

dormir()

next_page = driver.find_element_by_xpath('//*[text()="3"]')
next_page.click()

boton3 = driver.find_element_by_xpath('//i[@class="material-icons right"]')
dormir()
boton3.click()

boton4 = driver.find_element_by_xpath('//*[text()="Nivel 4"]')
dormir()
boton4.click()

dormir()

boton5 = driver.find_element_by_xpath('//a[@class="waves-effect waves-light btn"]')
boton5.click()
