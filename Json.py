import json

class exportarJson:

    """def guardar(diccionario, nombreArchivo="archivo.json"):
        with open(nombreArchivo, 'w') as archivo:
            json.dump(diccionario, archivo, indent=4)"""
    def guardar(lista_datos, nombre_archivo="archivo.json"):
            datos_exist = []
        
            try:
                #print(lista_datos)
                with open(nombre_archivo, 'r') as archivo:
                    datos_exist = json.load(archivo)
            except:
                pass
            

            lista_datos=lista_datos+datos_exist # Agregar los nuevos datos a los existentes
            lista2=[i for n, i in enumerate(lista_datos) if i not in lista_datos[n + 1:]]
            with open(nombre_archivo, 'w') as archivo:
                json.dump(lista2, archivo, indent=4)
    

    def importar(nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:
           diccionario = json.load(archivo)
        return diccionario