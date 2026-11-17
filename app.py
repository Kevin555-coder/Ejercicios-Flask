
## Importamos flask
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"
## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30% y 40% respectivamente.

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1*30)/100 + (nota2*30)/100 + (nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

## Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo
## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)

@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"

    return f"<h1>La persona es: {R}</h1> <hr>"

## Creamos otra ruta realizamos el siguiente ejemplo
## 3.) Programa que crea arreglos con los valores aleatorios
## Importamos la libreria numpy si no existe la instalamos con: pip install numpy

import numpy as np

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas == 0:
        arreglo = np.random.randint(valores, size=columnas)
    else:
        arreglo = np.random.randint(valores, size=(filas, columnas))

    return f"<h1>El arreglo aleatorio es: {arreglo}</h1><hr>"

## Creamos otra ruta para realizar la tabla de multiplicar
## ) Programa que captura un número y realiza
## la tabla de multiplicar hasta el 10

@app.route("/tabla")
@app.route("/tabla/<int:numero>")
def tabla(numero=0):

    resultado = ""

    for i in range(1, 11):
        multiplicacion = numero * i

        resultado += f"{numero} x {i} = {multiplicacion}<br>"

    return f"<h1>La tabla de multiplicar es:</h1>{resultado}<hr>"

# ) Programa que calcula las areas de un circulo,
## cuadrado y triangulo

import math

@app.route("/areas")
@app.route("/areas/<string:figura>/<float:valor1>")
@app.route("/areas/<string:figura>/<float:valor1>/<float:valor2>")
def areas(figura="circulo", valor1=0, valor2=0):

    if figura == "circulo":
        resultado = math.pi * (valor1 ** 2)
        R = f"El area del circulo es: {resultado:.2f}"

    elif figura == "cuadrado":
        resultado = valor1 * valor1
        R = f"El area del cuadrado es: {resultado:.2f}"

    elif figura == "triangulo":
        resultado = (valor1 * valor2) / 2
        R = f"El area del triangulo es: {resultado:.2f}"

    else:
        R = "Figura geometrica no valida"

    return f"<h1>{R}</h1><hr>"

if __name__ == "__main__":
    app.run(debug=True)

