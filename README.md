# Prueba automatizada (Tester1.pv)

## Introducción
Se hacesn varias puruebas de UnitTest muy básicas a la pag web solicitada de: app.sysdigcloud.com

## Requerimintos necesarios para la prueba
Fué necesario primero instalar los siguientes componetentes para dar inicio a la prueba:
1. Instalación de Python 3.9.6v / https://www.python.org/
2. Instalación del IDE de Pycharm / https://www.jetbrains.com/es-es/pycharm/ para poder programar sensillo con python, importante destacar que se incorpora el interprete de python y la paquetería de selenium según el requerimiento.
3. Configuración y descarga de los Webdrivers tanto para Chrome y el de Firefox, en el ejercicio se usa unicamente el de Chrome.

## Paso a apaso
1. Creamos el file Tester.py, importamos la librería de webdriver desde selenium y Keys para poder trabajar con el file
> import time

> import unittest

> from selenium import webdriver

> from selenium.webdriver.common.keys import Keys
>
> from selenium.webdriver.common.by import By

