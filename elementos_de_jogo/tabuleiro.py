"""
Módulo para a Classe Tabuleiro.
"""
class Tabuleiro:
    """
    Classe para tabuleiro do jogo.
    """

    __MAPA_CASAS = {
        1 : [0,0],
        2 : [0,1],
        3 : [0,2],
        4 : [1,0],
        5 : [1,1],
        6 : [1,2],
        7 : [2,0],
        8 : [2,1],
        9 : [2,2]
    }

    def __init__(self):
        self.__casas = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.__terminou = False
        self.__resultado = "Jogo em andamento"

        self.mostrar_tabuleiro()


    def __set_casa(self, casa: int, valor: str):

        l, c = self.__indexar_casa(casa)

        self.__casas[l][c] = valor


    def __indexar_casa(self, num_casa: int):
        return self.__MAPA_CASAS[num_casa][0], self.__MAPA_CASAS[num_casa][1]


    def mostrar_tabuleiro(self):

        print("Mapa casas\tTabuleiro")

        for l in range(0,3):

            print(end=f" |{(l+1)*3 - 2}|{(l+1)*3 - 1}|{(l+1)*3}|\t ")
            print(end="|")

            for c in range(0,3):

                conteudo = self.__casas[l][c]

                if conteudo:
                    print(end=f"{conteudo}|")
                else:
                    print(end=" |")

            print("\n")


    def get_casa(self, num_casa: int):

        linha, coluna = self.__indexar_casa(num_casa)

        return self.__casas[linha][coluna]


    def jogo_terminou(self):

        return self.__terminou


    def get_resultado(self):

        return self.__resultado


    def escolher_casa(self, casa: int, valor: str) -> bool:
        conteudo = self.get_casa(casa)

        if not conteudo:
            self.__set_casa(casa, valor)
            return True

        return False


    def confere_vitoria(self, linha: int, coluna: int, valor: str):

        # diagonal ou (linha ou coluna)
            # condicoes de vitória -> criar funcao para evitar repeticao
        if linha == coluna:

            if all(self.__casas[i][i] == valor for i in range(0,3)):
                self.__terminou = True
                self.__resultado = valor
