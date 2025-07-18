from lista_datos import ListaNumeros
from basededatos import BaseDatos

class Calculadora:
    def init(self):
        self.objlista = ListaNumeros()
        self.basedatos = BaseDatos()

    def Obtener_lista_numeros(self):
        entrada = input("Ingrese números separados por coma (ej: 1,2,3): ")
        try:
            return [int(x.strip()) for x in entrada.split(",")]
        except ValueError:
            print("Entrada inválida.")
            return []

    def menu(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Agregar dos números a la lista")
            print("2. Insertar número en posición específica")
            print("3. Eliminar número de la lista")
            print("4. Mostrar lista")
            print("5. Eliminar último número")
            print("6. Buscar índice")
            print("7. Contar repeticiones")
            print("8. Ordenar lista")
            print("9. Invertir lista")
            print("10. Crear tupla con pares")
            print("11. Crear tupla con impares")
            print("12. Ver tuplas")
            print("13. Modificar valor en tupla")
            print("14. Eliminar valor de tupla")
            print("15. Salir")

            opcion = input("Seleccione una opción (1-15): ")

            if opcion == "1":
                try:
                    n1 = float(input("Número 1: "))
                    n2 = float(input("Número 2: "))
                    self.objlista.incluir_lista([n1, n2])
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese números válidos.")

            elif opcion == "2":
                pos = int(input("Posición: "))
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                self.objlista.insertar_dato(pos, n2)
                self.objlista.insertar_dato(pos, n1)

            elif opcion == "3":
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                self.objlista.eliminar_dato(n1)
                self.objlista.eliminar_dato(n2)

            elif opcion == "4":
                self.objlista.ver_numero()

            elif opcion == "5":
                self.objlista.eliminar_ultimo()

            elif opcion == "6":
                num = float(input("Buscar número: "))
                self.objlista.buscar_indice(num)

            elif opcion == "7":
                num = float(input("Número a contar: "))
                self.objlista.contar_repetidos(num)

            elif opcion == "8":
                self.objlista.ordenar_lista()

            elif opcion == "9":
                self.objlista.invertir_lista()

            elif opcion == "10":
                nums = self.Obtener_lista_numeros()
                self.basedatos.Crear_tupla_numero_par(nums)

            elif opcion == "11":
                nums = self.Obtener_lista_numeros()
                self.basedatos.Crear_tupla_numero_impar(nums)

            elif opcion == "12":
                self.basedatos.ver_tuplas()

            elif opcion == "13":
                tipo = input("¿Modificar tupla 'par' o 'impar'?: ").lower()
                indice = int(input("Índice a modificar: "))
                nuevo = int(input("Nuevo valor: "))
                self.basedatos.modificar_valor(tipo, indice, nuevo)

            elif opcion == "14":
                tipo = input("¿Eliminar de tupla 'par' o 'impar'?: ").lower()
                valor = int(input("Valor a eliminar: "))
                self.basedatos.eliminar_valor(tipo, valor)

            elif opcion == "15":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "main":
    calc = Calculadora()
    calc.menu()