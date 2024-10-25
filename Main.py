import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget)
from PyQt6.uic.Compiler.qtproxies import QtWidgets


class PrimeraFiestra(QMainWindow):                                  ## Creamos una clase que hereda de QMainWindow
    contador = 0
    def __init__(self):                                             ## Constructor de la clase
        super().__init__()                                          ## Llamamos al constructor de la clase padre QMainWindow
        self.show()                                                 ## Mostramos la ventana
        self.setWindowTitle("EjemploQt: Primera Ventana")           ## Título de la ventana
        self.setMinimumSize(400, 200)                               ## Tamaño mínimo de la ventana
        self.setMaximumSize(800, 400)                               ## Tamaño máximo de la ventana

        ##Cambiamos el color de fondo
        pallete = self.palette()                                    ## Obtenemos la paleta de colores
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.lightGray) ## Cambiamos el color de fondo
        self.setPalette(pallete)                                    ## Aplicamos la paleta de colores

        ##Creamos el Layout
        caixaV = QVBoxLayout()                                      ## Creamos un Box Layout Vertical

        botonSaludar = QPushButton("Saludar")                       ## Creamos un botón
        botonSaludar.clicked.connect(self.saludar)    ## Conectamos la señal clicked al slot print("Hola Mundo")

        container = QWidget()                                       ## Creamos un widget contenedor

        container.setLayout(caixaV)                                 ## Establecemos el layout como contenido del widget contenedor
        self.setCentralWidget(container)                            ## Establecemos el layout como contenido central de la ventana
        caixaV.addWidget(botonSaludar)                              ## Añadimos el botón al layout

    def saludar(self):                                              ## Metodo que se ejecutará al hacer click en el botón
        print(f"Hola Mundo {self.contador}")                                         ## Imprimimos "Hola Mundo"
        self.contador += 1                                               ## Incrementamos el contador en 1



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraFiestra()
    aplicacion.exec()