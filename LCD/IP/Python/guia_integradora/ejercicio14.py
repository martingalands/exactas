# Ejercicio 14. Hospital - Alarma epidemiol´ogica
# Necesitamos detectar la aparici´on de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los
# registros de atenci´on por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad
# que motiv´o la atenci´on. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporci´on
# de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas
# cuya proporci´on supere cierto umbral.
# problema alarma epidemiologica (in registros : seq⟨Z × str⟩, in infecciosas : seq⟨str⟩, in umbral : R) : dict<str, R> {
# requiere: {0 < umbral < 1.}
# asegura: {claves de res pertenecen a infecciosas.}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
# }

def alarma_epidemiologica(registros:list[tuple[int,str]],infecciosas:list[str],umbral:float)->dict[str,float]:
    res:dict[str,float] = {}
    total_registros:int = 0
    #[(0.1,"ebola"),(0.3,"VIH")]

    for registro in registros:
        total_registros += registro[0]

    for registro in registros:
        cantidad_enfermos:int = registro[0]
        enfermedad:str = registro[1]
        porcentaje_enfermos:float = cantidad_enfermos/total_registros
        for enfermedad_infecciosa in infecciosas:
            if enfermedad_infecciosa == enfermedad and porcentaje_enfermos > umbral:
                res[enfermedad] = porcentaje_enfermos
    return res


print(alarma_epidemiologica([(26262,"ebola"),(553135,"VIH"),(25135135,"gripe"),(121513512,"lupus")],["VIH","ebola","lupus"],.001))


