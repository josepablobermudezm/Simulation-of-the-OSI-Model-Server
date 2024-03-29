from .aplicacion import aplicacion
class presentacion:

    def __init__(self, nombre):
        self.nombre = nombre


    def desencriptar(self,palabra):
        print("Desencriptando mensaje en la capa de Presentación")
        palabraAux = ""

        switcher = {
            "!_#": 'A',
            '@_(': 'B',
            '#_$': 'C',
            '$_*': 'D',
            '%_%': 'E',
            '^_-': 'F',
            '=_!': 'G',
            '~_&': 'H',
            '~_~': 'I',
            '-_-': 'J',
            '!_!': 'K',
            '$_^': 'L',
            '?_@': 'M',
            '/_/': 'N',
            '___': 'Ñ',
            '{_{': 'O',
            '}_}': 'P',
            ':_:': 'Q',
            '¿_?': 'R',
            ';_;': 'S',
            '&_!': 'T',
            '#_#': 'U',
            '*_*': 'V',
            '|_|': 'W',
            '°_°': 'X',
            'ü_ü': 'Y',
            '._.': 'Z',
            '...': ' '
        }

        indice = 0
        cont = 0
        l = ""
        while indice < len(palabra):
            if cont == 3:
                palabraAux += switcher.get(l, "???")
                l = ""
                cont = 0
            else:
                l += palabra[indice]
                cont += 1
                indice += 1
                if indice+1 == len(palabra):
                    l += palabra[indice]
                    palabraAux += switcher.get(l, "???")
        aplicacion.mostrarMensaje(None,palabraAux)#llamamos a la capa de aplicación para mostrar el mensaje
