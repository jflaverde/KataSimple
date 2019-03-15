
class SecuenciaNumeros:
    def procesarElementos(self, cadena):
        if cadena == "":
            return [0,0,0,0]
        else:
            numeros = cadena.split(",")
            intNumeros = map(int, numeros)

            return [len(numeros),min(intNumeros),0,0]

