
class SecuenciaNumeros:
    def procesarElementos(self, cadena):
        if cadena == "":
            return [0,0,0,0]
        else:
            cadena = cadena.replace("&",",")
            numeros = cadena.split(",")
            intNumeros = list(map(int, numeros))

            minimo = min(intNumeros)
            maximo = max(intNumeros)
            promedio = sum(intNumeros)/float(len(intNumeros))

            return [len(numeros),minimo,maximo,promedio]

