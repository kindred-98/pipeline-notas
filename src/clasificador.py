# src/clasificador.py

def clasificar_nota(nota):
    """Clasifica una nota numérica en su categoría.

    Reglas:
    - nota < 0 o nota > 10 → lanzar ValueError
    - 0 <= nota < 5 → "Suspenso"
    - 5 <= nota < 7 → "Aprobado"
    - 7 <= nota < 9 → "Notable"
    - 9 <= nota <= 10 → "Sobresaliente"
    """

    # Validación de rango
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10")

    # Clasificación
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"
