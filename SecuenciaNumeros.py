
class SecuenciaNumeros:
    def procesarElementos(self, cadena):
        if cadena == "":
            return [0,0,0,0]
        else:
            numeros = cadena.split(",")
            intNumeros = list(map(int, numeros))

            minimo = min(intNumeros)
            maximo = max(intNumeros)

            return [len(numeros),minimo,maximo,0]

