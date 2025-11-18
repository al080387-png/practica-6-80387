# Modulo: calculo_resistencia.py

def calcular_resistencia(fprima_c, tipo_cemento="Ordinario", edad=28):
    """
    Calcula la resistencia del concreto a partir de la resistencia a los 28 días (f'c),
    considerando el tipo de cemento y la edad.

    Parámetros:
    - fprima_c (float): Resistencia especificada del concreto a los 28 días (MPa).
    - tipo_cemento (str, opcional): Tipo de cemento utilizado ("Ordinario", "Rápido", "Resistente a sulfatos"). Por defecto es "Ordinario".
    - edad (int, opcional): Edad del concreto en días. Por defecto es 28.

    Retorna:
    - float: Resistencia estimada del concreto a la edad especificada (MPa).
    """

    # Factor de ajuste por tipo de cemento
    factores_cemento = {
        "Ordinario": 1.0,
        "Rápido": 1.15,
        "Resistente a sulfatos": 0.9
    }
    factor_cemento = factores_cemento.get(tipo_cemento, 1.0)  # Usar 1.0 por defecto si el tipo no es reconocido

    # Ajuste por edad (aproximación logarítmica)
    factor_edad = calcular_factor_edad(edad)

    # Cálculo de la resistencia
    resistencia = fprima_c * factor_cemento * factor_edad
    return resistencia

def calcular_factor_edad(edad):
    """
    Calcula el factor de ajuste por edad usando una aproximación logarítmica.

    Parámetros:
    - edad (int): Edad del concreto en días.

    Retorna:
    - float: Factor de ajuste por edad.
    """
    if edad < 28:
        factor_edad = (edad / 28)**0.5
    else:
        factor_edad = 1.0
    return factor_edad

def main():
    """
    Función principal para interactuar con el usuario y calcular la resistencia del concreto.
    """
    fprima_c = float(input("Ingrese la resistencia especificada del concreto a los 28 días (f'c) en MPa: "))
    tipo_cemento = input("Ingrese el tipo de cemento (Ordinario, Rápido, Resistente a sulfatos): ")
    edad = int(input("Ingrese la edad del concreto en días: "))

    resistencia_calculada = calcular_resistencia(fprima_c, tipo_cemento, edad)
    print(f"La resistencia estimada del concreto a los {edad} días es: {resistencia_calculada:.2f} MPa")

if __name__ == "__main__":
    main()
    
