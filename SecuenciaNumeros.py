
class SecuenciaNumeros:
    def procesarElementos(self, cadena):
        if cadena == "":
            return [0,0,0,0]
        else:
            numeros = cadena.split(",")
            return [len(numeros),0,0,0]

