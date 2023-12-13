from listaMetodos import Lista
from Json import exportarJson
import datetime

class Datos(Lista):
    def __init__(self,tipo="", nSensor="", valor= ""):
        super().__init__()
        self.tipo = tipo
        self.nSensor = nSensor
        self.valor = valor
        self.archivo = "Datos.json"
        
        

    def __str__(self):
        if len(self.lista)>1:
            return f'Contiene {len(self.lista)} elementos'
        return f'{str(self.tipo).ljust(5)} \t\t\t| {self.nSensor.ljust(5)} \t\t\t| {self.valor.ljust(5)}'

    def guardar(self):
        exportarJson.guardar(self.Diccionario(),self.archivo)
             
    
    #def convertirJson(self,lista):
        #print("funciones: ", lista)
         
     #   for datos in lista:
      #      id = datos.get('id')
       #     puertos = datos.get('puertos')
        #    descripcion = datos.get('descripcion')
         #   sensorDatos = Datos(id,puertos,descripcion)
          #  self.crear(sensorDatos)
    
    #def importar(self):
     #       Dic = exportarJson.importar(self.archivo)
      #      self.convertirJson(Dic)
            
    
    def Diccionario(self):
        diccionario_datos = []
        #print(self.lista)
       
        for sensor in self.lista:
                    #print(sensor)
                    
            diccionario_sensor = {
                'tipo': sensor.get('tipo'),
                'nSensor': sensor.get('nSensor'),
                'valor': sensor.get('valor'),           
                }
            diccionario_datos.append(diccionario_sensor)
        return diccionario_datos

if __name__ == '__main__':
     
    DatosL = Datos()
    DatosL.guardar()