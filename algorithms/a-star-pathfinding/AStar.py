import numpy as np

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class Grafo:
    arad = Vertice('Arad', 366)
    bucharest = Vertice('Bucharest', 0)
    craiova = Vertice('Craiova', 160)
    drobeta = Vertice('Drobeta', 242)
    eforie = Vertice('Eforie', 161)
    fagaras = Vertice('Fagaras', 176)
    giurgiu = Vertice('Giurgiu', 77)
    hirsova = Vertice('Hirsova', 151)
    lasi = Vertice('Hirsova', 226)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    neamt = Vertice('Neamt', 234)
    oradea = Vertice('Oradea', 380)
    pitesti = Vertice('Pitesti', 100)
    rimnicu = Vertice('Rimnicu', 193)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    uziceni = Vertice('Uziceni', 80)
    vaslui = Vertice('Vaslui', 199)
    zerind = Vertice('Zerind', 374)

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(drobeta, 75))

    drobeta.adiciona_adjacente(Adjacente(mehadia, 75))
    drobeta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(drobeta, 120))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(uziceni, 85))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

    giurgiu.adiciona_adjacente(Adjacente(bucharest, 90))

    uziceni.adiciona_adjacente(Adjacente(bucharest, 85))
    uziceni.adiciona_adjacente(Adjacente(vaslui, 142))
    uziceni.adiciona_adjacente(Adjacente(hirsova, 98))

    hirsova.adiciona_adjacente(Adjacente(uziceni, 98))
    hirsova.adiciona_adjacente(Adjacente(eforie, 86))

    eforie.adiciona_adjacente(Adjacente(hirsova, 86))

    vaslui.adiciona_adjacente(Adjacente(uziceni, 142))
    vaslui.adiciona_adjacente(Adjacente(lasi, 92))

    lasi.adiciona_adjacente(Adjacente(vaslui, 92))
    lasi.adiciona_adjacente(Adjacente(neamt, 87))

    neamt.adiciona_adjacente(Adjacente(lasi, 87))

grafo = Grafo()

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)
    
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ': ',
                self.valores[i].custo, ' - ',
                self.valores[i].vertice.distancia_objetivo, ' - ',
                self.valores[i].distancia_aestrela)

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self. encontrado = False
    
    def buscar(self, atual):
        print('-------------')
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjascente in atual.adjacentes:
                if adjascente.vertice.visitado == False:
                    adjascente.vertice.visitado = True
                    vetor_ordenado.insere(adjascente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)

busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.lugoj)