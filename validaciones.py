# validaciones.py

def validar_codigo_expediente(texto: str) -> str:
    """Normaliza la cadena de texto y valida el formato estricto EXP-###"""
    codigo = texto.strip().upper()  # Manipulación de cadenas: limpiar espacios y convertir a mayúsculas
    partes = codigo.split("-")      # Descomposición de cadenas (split)
    
    if len(partes) != 2 or partes[0] != "EXP" or not partes[1].isdigit() or len(partes[1]) != 3:
        raise ValueError("Código inválido. Formato requerido: EXP-001")
    return codigo

def validar_documento_ciudadano(doc: str) -> str:
    """Valida que el documento ingresado sea DNI (8 dígitos) o RUC (11 dígitos)"""
    doc_limpio = doc.strip()
    if not doc_limpio.isdigit() or len(doc_limpio) not in (8, 11):
        raise ValueError("Documento incorrecto. Debe tener 8 dígitos (DNI) u 11 dígitos (RUC).")
    return doc_limpio


# Bloque de pruebas independientes para la terminal
if __name__ == "__main__":
    print("--- PRUEBAS DEL MÓDULO VALIDACIONES ---")
    try:
        res1 = validar_codigo_expediente("  exp-001  ")
        print(f"Prueba 1 Exitosa -> Resultado: {res1}")
    except ValueError as e:
        print(f"Prueba 1 Fallida -> Error: {e}")

    try:
        validar_codigo_expediente("123-EXP")
    except ValueError as e:
        print(f"Prueba 2 Capturada con éxito -> Error: {e}")