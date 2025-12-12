from conexion import ConexionBD

class DPersona:
    def __init__(self):
        self.__db = ConexionBD().conexionSupabase()
        self.__nombretabla = 'persona'

    def __ejecutarConsulta(self, consulta, tipoConsulta = None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
            else:
                resultado = consulta.esecute()
            return resultado
        except Exception as e:
            return f'Error {e}'

    def mostrarPersona(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')
    
    def insertarPersona(self, persona: dict):
        consulta = self.__db.table(self.__nombretabla).insert(persona)
        return self.__ejecutarConsulta(consulta)
    
    def actualizarPersona(self, persona: dict, docIdentidad: str):
        consulta = self.__db.table(self.__nombretabla).update(persona).eq('docIdentidad',docIdentidad)
        return self.__ejecutarConsulta(consulta)

    def eliminarPersona(self, docIdentidad: str):
        consulta = self.__db.table(self.__nombretabla).delete().eq('docIdentidad', docIdentidad)
        return self.__ejecutarConsulta(consulta)