# Prueba automatizada (Tester1.py)

## Introducci贸n
Se hacen varias pruebas de UnitTest muy b谩sicas a la pag web solicitada de: app.sysdigcloud.com

## Requerimientos necesarios para la prueba 馃敡
Fu茅 necesario primero instalar los siguientes componentes para dar inicio a la prueba:
1. Instalaci贸n de Python 3.9.6v / https://www.python.org/
2. Instalaci贸n del IDE de Pycharm / https://www.jetbrains.com/es-es/pycharm/ para poder programar sencillo con python, importante destacar que se incorpora el interprete de python y la paqueter铆a de selenium seg煤n el requerimiento.
3. Configuraci贸n y descarga de los Webdrivers tanto para Chrome y el de Firefox, en el ejercicio se usa unicamente el de Chrome.

## Paso a paso 馃殌
1. Creamos el proyecto **Norberto** con el file **Tester1.py**, importamos las siguientes librerias necesarias para la prueba, en el caso de **unittest se incorpora    sola**

> import time
>
> import unittest
>
> from selenium import webdriver
>
> from selenium.webdriver.common.keys import Keys
>
> from selenium.webdriver.common.by import By

2. Creamos una clase llamada **prueba** la cual nos importa la libreria de unittest automatico, creamos la funci贸n que debe llamarce **def** con el argumento **self** y para usarlo podemos poner una variable en este caso se llama drive para llamar la ruta de Chrome con .get.

Tratamos de usar Unittest para orden del c贸digo, el cual seria como la mejor manera de crear una plantilla para futuros test

>class prueba(unittest.TestCase):
>   def setUp(self):
>       self.driver = webdriver.Chrome('chromedriver.exe')

3. Creamos el primer **Test_login1** 鈿欙笍
La idea de este test es abrir la pagina web en Chrome y utilizando el Selector id de email addrees (ember1642) enviamos con Keys el dato de un correo electronico de ejemplo, luego utilizando el Selector id de password (ember1643) enviamos con Keys el dato de una clave cualquiera, posterior utilizando el Selector id de Log-in    (ember1652) e invocamos un click para que oprima en la casilla e imprimimos un mensaje de error de credenciales, incluyo un timer de 3 segundo solo para poder        visualizar los detalles:
   
> def test_login1(self):
>    driver = self.driver
>    
>    driver.get('https://app.sysdigcloud.com/#/login')
>    
>    email = driver.find_element(By.ID, 'ember1642')
>    
>    email.send_keys("norberto.araya@gmail.com")
>    
>    clave = driver.find_element(By.ID, 'ember1643')
>    
>    clave.send_keys("Clave1234")
>    
>    bto = driver.find_element(By.ID, 'ember1652')
>    
>    bto.click()
>    
>    print("error crendenciales incorrectas")
>    
>    time.sleep(3)

4. Creamos el segundo **Test_login2** 鈿欙笍
   La idea de este test es abrir la pagina web en Chrome y utilizando el Selector id de email addrees (ember1642) enviamos con Keys el dato de un correo electronico      vacio, luego utilizando el Selector id de password (ember1643) enviamos con Keys el dato de una clave vacia, posterior utilizando el Selector id de Log-in              (ember1652) e invocamos un click para que oprima en la casilla e imprimimos un mensaje de error por fata de datos, incluyo un timer de 3 segundo solo para poder        visualizar los detalles:
   
> def test_login2(self):
>    driver = self.driver
>    
>    driver.get('https://app.sysdigcloud.com/#/login')
>    
>    email = driver.find_element(By.ID, 'ember1642')
>    
>    email.send_keys("")
>    
>    clave = driver.find_element(By.ID, 'ember1643')
>    
>    clave.send_keys("")
>    
>    bto = driver.find_element(By.ID, 'ember1652')
>    
>    bto.click()
>    
>    print("error de login por no colocar datos")
>    
>    time.sleep(3)

5. Creamos el tercer **Test_login3** 鈿欙笍
   En este test se trata de abrir la pagina web en Chrome y utilizando el Selector id de Log in with Google (identifierId) enviamos con Keys el dato de un correo          electronico de ejemplo, luego utilizando el Selector id de password (V67aGc) enviamos con Keys el dato de una clave vacia, posterior utilizando el Selector id de      jsname="V67aGc"e invocamos un click para que oprima en la casilla e imprimimos un mensaje de credencial incorrecto, incluyo un timer de 3 segundo solo para poder      visualizar los detalle:
   
> def test_login3(self)
> 
> driver = self.driver
> 
> driver.get('https://app.sysdigcloud.com/api/oauth/google?redirectRoute=/')
> 
> identi = driver.find_element(By.ID, 'identifierId')
> 
> identi.send_keys("norberto.araya@gmail.com")
> 
> bto = driver.find_element(By.ID, 'V67aGc')
> 
> bto.click()
> 
> print("error credenciales incorrectas")
> 
>time.sleep(3)

> **NOTA: En este caso no logre aclarar bien el tema del Selector correcto para llamar la tecla siguiente = jsname="V67aGc"**

6. Creamos la funcion final para el cierre de la prueba de **Tester1**, debe llamarse **tearDown** y se agraga un if name == main que unittest en su plantilla oficial pide como requisito base para cerrar la clase principal:

>def tearDown(self):
>
>       driver = self.driver
>       
>       driver.close()
>
>if __name__ == '__main__':
>
>   unittest.main()

## Posibles mejoras si hubiera m谩s tiempo 馃敥
1. La mejora que hubiese incorporado es hacer que la prueba se completara correcta desde la class "prueba", existe un error con esa clase que debo revisar, sin       embargo, cada test si se ejecuta individual si funciona.
2. Me hubise gusta incorporar el selector correcto para llamar la casilla "siguiente" el la prueba de login con Google, se que us茅 uno icorrecto, no devio ser de ID para jsname="V67aGc.
3. Adem谩s me hubiera gusta hacer alguna pruebas mas detalladas con el login de google,salm y OpenID
4. En general talvez me viera gustado introducir otros selectores como XPHAH, AND incluso un if viera sido muy interesante y util para la prueba m谩s automatizada

## Autor 鉁掞笍
Norberto Araya Mena

