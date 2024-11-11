{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOgjeMrdE27b2OB0+WbqzbD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Jorge-742/TalenTech_Exercise_Practice/blob/main/Laboratorio_6_fund_python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Ejercicios Python Laboratorio 6\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "HQttROKlkbVj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. **Algoritmo para Preparar un Té**: Este algoritmo describe los pasos para preparar un té\n",
        "y lo implementamos en Python.\n",
        "\n",
        "*   Pasos:\n",
        "    1. Calentar el agua.\n",
        "    2. Colocar una bolsa de té en un taza.\n",
        "    3. Echar el agua caliente dentro del taza.\n",
        "    4. Revolver con una cuchara.\n",
        "    5. listo para tomar.\n",
        "\n",
        "* Código:"
      ],
      "metadata": {
        "id": "rZ25ILnSk8PC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Algoritmo en versión código\n",
        "\n",
        "agua_caliente = True\n",
        "bolsa_te = True\n",
        "if agua_caliente and bolsa_te:\n",
        "    print('Coloca el té en la taza')\n",
        "    print('Echa el agua caliente dentro de la taza')\n",
        "    print('Mezcla con una cuchara')\n",
        "    print('Listo para tomar')\n",
        "else:\n",
        "    print('No puedes tomar té sino tienes agua caliente y bolsas de té.')"
      ],
      "metadata": {
        "id": "yXt_OrDFkacE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0859a99d-d985-4825-eb43-038ff8425aaf"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Coloca el té en la taza\n",
            "Echa el agua caliente dentro de la taza\n",
            "Mezcla con una cuchara\n",
            "Listo para tomar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "PkI3R4-f_Yrx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Cálculo del Promedio de Notas: Utilizar variables y tipos de datos para almacenar las notas de un estudiante, y un operador aritmético para calcular el promedio.\n",
        "\n",
        "- Pasos:\n",
        "  1. Definir variables para almacenar las notas.\n",
        "  2. ingreso de notas.\n",
        "  3. formula para calcular promedio.\n",
        "  4. Imprimir resultado en pantalla.\n",
        "\n",
        "* Código:\n"
      ],
      "metadata": {
        "id": "hnmLPEU4lweL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Cálculo de promedio de notas\n",
        "\n",
        "nota_1 = float(input('Ingrese su nota: '))\n",
        "nota_2 = float(input('Ingrese su nota: '))\n",
        "nota_3 = float(input('Ingrese su nota: '))\n",
        "\n",
        "promedio = (nota_1 + nota_2 + nota_3) / 3\n",
        "\n",
        "print(f'Su promedio es: {promedio}')"
      ],
      "metadata": {
        "id": "eJ5zhwJp_4Af",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2e1eb49c-f22e-4b7f-c8f6-69e431942ef2"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese su nota: 8\n",
            "Ingrese su nota: 4\n",
            "Ingrese su nota: 5\n",
            "Su promedio es: 5.666666666666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "n9iZEhfKBbJi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Verificar si un Número es Par o Impar: Utiliza condicionales para verificar si un número es par o impar, y operadores para realizar el cálculo.\n",
        "\n",
        "- Pasos:\n",
        "  1. Definir vaiable e input.\n",
        "  2. Formúla para verificar si el número es par o impar.\n",
        "  3. Impresión en pantalla del resultado.\n",
        "\n",
        "- Código:"
      ],
      "metadata": {
        "id": "xsh-39-6Bc2M"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Verificador de números pares e impares\n",
        "\n",
        "numero = int(input('Ingrese un número: '))\n",
        "\n",
        "if numero % 2 == 0:\n",
        "    print(f'El número {numero} es par')\n",
        "else:\n",
        "    print(f'El número {numero} es impar')"
      ],
      "metadata": {
        "id": "zjjl-hJKCXfV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b209ee83-f9f8-4f3b-ee0e-2cfc29a5b15f"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese un número: 5\n",
            "El número 5 es impar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "---"
      ],
      "metadata": {
        "id": "11DiVrfnDG-7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Bucle for para Imprimir Números del 1 al 5: Usar un bucle for para mostrar los números del 1 al 5 y combinar los operadores aritméticos para mostrar si son pares o impares.\n",
        "- Pasos:\n",
        "  1. definir la variable.\n",
        "  2. Crear el bucle for con un rango de números del 1 al 6.\n",
        "  3. Crear el condicional if para verificar si el número es par o impar.\n",
        "  4. Imprimir en pantalla los números y su texto identificador.\n",
        "\n",
        "- Código:"
      ],
      "metadata": {
        "id": "-tFFT26DDNKu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Impresora de números\n",
        "\n",
        "numero = 0\n",
        "\n",
        "for numero in range(1,6):\n",
        "    if numero % 2 == 0:\n",
        "      print(f'El número {numero} es par')\n",
        "    else:\n",
        "      print(f'El número {numero} es impar')"
      ],
      "metadata": {
        "id": "Pt8gYeS3EYmD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4468c15f-2e49-494a-b77c-180a96b2f9a9"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El número 1 es impar\n",
            "El número 2 es par\n",
            "El número 3 es impar\n",
            "El número 4 es par\n",
            "El número 5 es impar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "612ZRX06FwRi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Convertir Grados Celsius a Fahrenheit: Usar una función para convertir grados Celsius a Fahrenheit. La fórmula para la conversión es Fahrenheit = (Celsius * 9/5) + 32.\n",
        "- Pasos:\n",
        "  1. Definir variable con input para celcius.\n",
        "  2. Asignar la formula de conversión a una variable.\n",
        "  3. Imprimir resultado en pantalla.\n",
        "- Código:"
      ],
      "metadata": {
        "id": "1EcmKa4AFzo2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Conversor de temperatura\n",
        "\n",
        "celsius = float(input('Ingrese la temperatura en Celsius: '))\n",
        "\n",
        "fahrenheit = (celsius * 9/5) + 32\n",
        "\n",
        "print(f'La temperatura en Fahrenheit es: {fahrenheit}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RPNfD0A_F03M",
        "outputId": "1f61c675-1183-459f-c3ee-7ff32f1c60d1"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese la temperatura en Celsius: 30\n",
            "La temperatura en Fahrenheit es: 86.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "1bII1cwnHmg9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Contar la Cantidad de Vocales en una Cadena de Texto: Utilizar un bucle for y una condicional para contar cuántas vocales hay en una cadena de texto ingresada por el usuario.\n",
        "- Pasos:\n",
        "  1. Definir variable de conteo.\n",
        "  2. Asignar el input a una variable.\n",
        "  3. Crear el bucle for para iterar sobre la cadena de texto.\n",
        "  4. Crear la condicional para la sumatoria de las vocales gracias a la iteración del bucle for.\n",
        "  4. Imprimir resultado en pantalla.\n",
        "  \n",
        "- Código:"
      ],
      "metadata": {
        "id": "0mwxPNOqHoju"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Contador de vocales\n",
        "\n",
        "num_vocales = 0\n",
        "texto = input('Ingrese un texto: ')\n",
        "\n",
        "for letra in texto:\n",
        "    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':\n",
        "        num_vocales += 1\n",
        "print(f'El número total de vocales es de: {num_vocales}')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cZWqolehHpaR",
        "outputId": "fc8d41f7-f786-439a-a36b-4205ccc58e57"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese un texto: ciencia de datos\n",
            "El número total de vocales es de: 7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "5uPl_PfbMumq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. Calcular el Factorial de un Número: Usar un bucle while para calcular el factorial de un número ingresado por el usuario. El factorial de un número n (n!) es el producto de todos los números enteros positivos menores o iguales a n.\n",
        "- Pasos:\n",
        "    1. Definir variables. factorial en 1. numero para el ingreso del input, es decir, del número al que se le calcula el factorial.\n",
        "    2. Crear el bucle While el cual va a iterar sobre el valor de la variable numero mientras que está sea mayor a 1.\n",
        "    3. Se aplica la formula para los factoriales.\n",
        "    4. Se imprime en pantalla el resultado.\n",
        "\n",
        "- Código:"
      ],
      "metadata": {
        "id": "YyNulELNMxyH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Factorial de un número\n",
        "\n",
        "factorial = 1\n",
        "numero = int(input('Ingrese un número: '))\n",
        "\n",
        "while numero > 1:\n",
        "    factorial *= numero\n",
        "    numero -= 1\n",
        "\n",
        "print(f'El factorial del número ingresado es: {factorial}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AMiYM44KMzcw",
        "outputId": "7eca5edb-903e-4558-f9f0-75fab49fc6b8"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese un número: 9\n",
            "El factorial del número ingresado es: 362880\n"
          ]
        }
      ]
    }
  ]
}