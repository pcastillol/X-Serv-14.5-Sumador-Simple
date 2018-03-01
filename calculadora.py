#!/usr/bin/python3

import sys

def suma(op1, op2):
    return op1 + op2

def resta(op1, op2):
    return op1 - op2

def mult(op1, op2):
    return op1 * op2

def div(op1, op2):
    try:
        return op1 / op2
    except ZeroDivisionError:
        return("No intentes dividir entre 0")


funciones = {
    'suma': suma,
    'resta': resta,
    'multiplicacion': mult,
    'division': div
    }


if __name__ == '__main__':

    NUM_ARG = 4

    if len(sys.argv) != NUM_ARG:
         sys.exit("Error. Uso: python3 calculadora.py funcion operando1 operando2")

    _, funcion, operando1, operando2 = sys.argv

    try:
        op1 = float(operando1)
        op2 = float(operando2)
        resultado = funciones[funcion](op1, op2)
    except ValueError:
        sys.exit("No es posible operar con chars")
    except KeyError:
        sys.exit("No existe la funcion " + funcion)

    print(str(resultado))
