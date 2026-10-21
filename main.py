# main.py
from validaciones import validar_codigo_expediente, validar_documento_ciudadano
from ordenamiento import busqueda_binaria_expediente, obtener_indices_ordenados

def ejecutar_sistema():
    # Arreglos paralelos para almacenar los datos del trámite documentario
    codigos = []
    documentos = []
    remitentes = []
    asuntos = []
    areas = []

    while True:
        print("\n========================================")
        print("   SISTEMA MESA DE PARTES DIGITAL (EP)   ")
        print("========================================")
        print("1. Registrar nuevo expediente")
        print("2. Consultar expediente por código (Búsqueda Binaria)")
        print("3. Listar expedientes registrados")
        print("4. Salir del programa")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- REGISTRO DE EXPEDIENTE ---")
            try:
                raw_codigo = input("Ingrese el código del expediente (Ej: EXP-001): ")
                codigo = validar_codigo_expediente(raw_codigo)
                
                if codigo in codigos:
                    print(f"Error: El código '{codigo}' ya se encuentra registrado.")
                    continue
            except ValueError as err:
                print(f"Error de validación: {err}")
                continue

            try:
                raw_doc = input("Ingrese DNI (8 dígitos) o RUC (11 dígitos) del ciudadano: ")
                documento = validar_documento_ciudadano(raw_doc)
            except ValueError as err:
                print(f"Error de validación: {err}")
                continue

            remitente = input("Ingrese el nombre del remitente: ").strip()
            asunto = input("Ingrese el asunto del trámite: ").strip()
            area = input("Ingrese el área de destino: ").strip()

            codigos.append(codigo)
            documentos.append(documento)
            remitentes.append(remitente)
            asuntos.append(asunto)
            areas.append(area)

            print(f"\n¡Éxito! Expediente {codigo} registrado correctamente.")

        elif opcion == "2":
            print("\n--- CONSULTA DE EXPEDIENTE ---")
            if len(codigos) == 0:
                print("No hay expedientes registrados en el sistema.")
                continue
            
            buscado = input("Ingrese el código del expediente a buscar (Ej: EXP-001): ").strip().upper()
            
            indices_ordenados = obtener_indices_ordenados(codigos)
            codigos_ordenados = [codigos[i] for i in indices_ordenados]
            
            pos_ordenada = busqueda_binaria_expediente(codigos_ordenados, buscado)
            
            if pos_ordenada != -1:
                pos_real = indices_ordenados[pos_ordenada]
                print("\n[!] ¡EXPEDIENTE ENCONTRADO!")
                print(f"Código     : {codigos[pos_real]}")
                print(f"Documento  : {documentos[pos_real]}")
                print(f"Remitente  : {remitentes[pos_real]}")
                print(f"Asunto     : {asuntos[pos_real]}")
                print(f"Área       : {areas[pos_real]}")
            else:
                print(f"\n[X] No se encontró ningún registro con el código '{buscado}'.")

        elif opcion == "3":
            print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
            if len(codigos) == 0:
                print("No hay expedientes registrados.")
            else:
                print(f"Total de trámites en sistema: {len(codigos)}")
                print("-" * 55)
                for i in range(len(codigos)):
                    print(f"[{i+1}] Código: {codigos[i]} | Doc: {documentos[i]} | Remitente: {remitentes[i]}")
                print("-" * 55)

        elif opcion == "4":
            print("\nFinalizando prototipo de Evaluación Parcial.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_sistema()