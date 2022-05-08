#  Importamos las librerias necesarias
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class prueba(unittest.TestCase):
    #  Declaramos variable drive para webdriver y colocamos a que brouser vamos a usar
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_login1(self):
        driver = self.driver
        driver.get('https://app.sysdigcloud.com/#/login')
        email = driver.find_element(By.ID, 'ember1642')
        email.send_keys("norberto.araya@gmail.com")
        clave = driver.find_element(By.ID, 'ember1643')
        clave.send_keys("Clave1234")
        bto = driver.find_element(By.ID, 'ember1652')
        bto.click()
        print("error crendenciales incorrectas")
        time.sleep(3)

    def test_login2(self):
        driver = self.driver
        driver.get('https://app.sysdigcloud.com/#/login')
        email = driver.find_element(By.ID, 'ember1642')
        email.send_keys("")
        clave = driver.find_element(By.ID, 'ember1643')
        clave.send_keys("")
        bto = driver.find_element(By.ID, 'ember1652')
        bto.click()
        print("error de login por no colocar datos")
        time.sleep(3)

    def test_login3(self):
        driver = self.driver
        driver.get('https://app.sysdigcloud.com/api/oauth/google?redirectRoute=/')
        identi = driver.find_element(By.ID, 'identifierId')
        identi.send_keys("norberto.araya@gmail.com")
        bto = driver.find_element(By.ID, 'V67aGc')
        bto.click()
        print("error credenciales incorrectas")
        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':

    unittest.main()