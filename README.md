# practica-6-80387
Objetivo del Programa
El objetivo principal de este programa es calcular la resistencia del concreto a una edad específica, considerando la resistencia especificada a los 28 días (conocida como f'c), el tipo de cemento utilizado y la edad del concreto.
Componentes Clave del Código
El código se compone de tres partes principales:
Función calcular_resistencia(fprima_c, tipo_cemento="Ordinario", edad=28)
Función calcular_factor_edad(edad)
Función main()
Vamos a analizar cada una de estas partes en detalle.
1. Función calcular_resistencia
Esta función es el corazón de nuestro programa. Recibe tres parámetros:
fprima_c (float): Es la resistencia especificada del concreto a los 28 días, medida en MPa (megapascales). Este valor es fundamental porque representa la resistencia de diseño del concreto.
tipo_cemento (str, opcional): Indica el tipo de cemento utilizado en la mezcla de concreto. Los tipos de cemento que consideramos son "Ordinario", "Rápido" y "Resistente a sulfatos". Por defecto, si no se especifica un tipo, asumimos que es "Ordinario".
edad (int, opcional): Representa la edad del concreto en días. Por defecto, se considera 28 días, que es el estándar para medir la resistencia de diseño.
¿Cómo funciona?
Factor de Ajuste por Tipo de Cemento:
Utilizamos un diccionario llamado factores_cemento para ajustar la resistencia según el tipo de cemento. Cada tipo de cemento tiene un factor asociado que modifica la resistencia base. Por ejemplo:
Cemento Ordinario: Factor de 1.0 (no modifica la resistencia).
Cemento Rápido: Factor de 1.15 (aumenta la resistencia).
Cemento Resistente a sulfatos: Factor de 0.9 (disminuye la resistencia).
Si el tipo de cemento ingresado no se encuentra en el diccionario, se utiliza un factor de 1.0 por defecto.
Ajuste por Edad:
La resistencia del concreto varía con el tiempo. Para tener en cuenta este factor, llamamos a la función calcular_factor_edad(edad) que calcula un factor de ajuste basado en la edad del concreto.
Cálculo Final:
Finalmente, la función calcula la resistencia estimada del concreto multiplicando la resistencia especificada (fprima_c) por el factor de ajuste del tipo de cemento y el factor de ajuste por edad.
La fórmula es:
Resistencia Estimada = fprima_c * factor_cemento * factor_edad
2. Función calcular_factor_edad
Esta función calcula el factor de ajuste por edad, que es crucial porque el concreto no alcanza su resistencia máxima inmediatamente.
Parámetro edad (int): La edad del concreto en días.
¿Cómo funciona?
Edad Menor a 28 Días:
Si la edad del concreto es menor a 28 días, utilizamos una aproximación logarítmica para estimar el desarrollo de la resistencia. La fórmula es:
factor_edad = (edad / 28)**0.5
Esta fórmula se basa en la observación de que la resistencia del concreto aumenta rápidamente en las primeras semanas y luego se estabiliza.
Edad Mayor o Igual a 28 Días:
Si la edad del concreto es 28 días o más, asumimos que la resistencia ha alcanzado su valor de diseño y el factor de ajuste es 1.0.
factor_edad = 1.0
3. Función main
La función main es el punto de entrada del programa. Es la que se ejecuta cuando corremos el script.
¿Qué hace?
Solicita Datos al Usuario:
Pide al usuario que ingrese la resistencia especificada del concreto a los 28 días (fprima_c), el tipo de cemento y la edad del concreto.
Utiliza la función input() para obtener estos valores del usuario.
Llama a la Función calcular_resistencia:
Llama a la función calcular_resistencia con los valores proporcionados por el usuario para calcular la resistencia estimada del concreto.
Muestra el Resultado:
Imprime el resultado en la consola, formateado a dos decimales, para que sea fácil de leer.
Ejemplo de Uso
Si ejecutamos el programa e ingresamos los siguientes datos:
Resistencia especificada (f'c): 25 MPa
Tipo de cemento: Ordinario
Edad del concreto: 35 días
El programa calculará la resistencia estimada como:
Resistencia Estimada = 25 MPa * 1.0 * 1.0 = 25.00 MPa
Limitaciones
Es importante tener en cuenta que este programa proporciona una estimación básica. Para cálculos más precisos, se deben considerar otros factores como:
La composición exacta de la mezcla de concreto.
Las condiciones de curado (temperatura, humedad).
Los resultados de pruebas de laboratorio específicas.
Conclusión
Este programa es una herramienta útil para obtener una estimación rápida de la resistencia del concreto. Sin embargo, siempre es recomendable complementar estos cálculos con pruebas y análisis más detallados para garantizar la seguridad y durabilidad de las estructuras.
