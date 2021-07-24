import time
import collections

class Vertice:
	def __init__(self, vertice, distancia, coordenadas):
		self.vertice = vertice
		self.distancia = distancia
		self.coordenadas = coordenadas
		self.ja_conheco = False

knightPos = 0 
endPos = 0

def readG(name): 
  nodos1 = {}
  adjacencyList = collections.defaultdict(set)
  
  dx = [ -2, -1, 1, 2, -2, -1, 1, 2 ]
  dy = [ -1, -2, -2, -1, 1, 2, 2, 1 ]
  heightC = 0
  lengthR = 0

  with open(name, 'r') as fp:
    global endPos
    global knightPos
    c = 0
    for lin in fp :
      r = 0
      lin = lin.rstrip()
      words = list(lin)
      for vertice in words:
        novoNodo = Vertice(vertice, 0, (c,r))
        if vertice != 'x':
          nodos1[c,r] = novoNodo
          if vertice == 'S':
            endPos = novoNodo          
          elif vertice == 'C':
            knightPos = novoNodo

        r += 1
      lengthR = r
      heightC += 1
      c += 1

    #lengthR = lengthR -1
    #heightC = heightC -1

    for nodo in nodos1:
      listaArestas = set()
      for i in range(7):
        newC = nodo[0] + dx[i]
        if newC < 0:
          newC = newC + heightC 
          #SE EU TIRO O -1 FICA O RESULTADO DA FERNANDA E GABRIELA
        if newC > heightC-1:
          newC = newC - heightC

        newR = nodo[1] + dy[i]
        if newR < 0:
          newR = newR + lengthR 
        if newR > lengthR-1:
          newR = newR - lengthR

        #TODO TALVEZ POSSA SER MELHORADO ESTE IF QUE É UM FOR!!!`
        if (newC, newR) in nodos1:
          listaArestas.add(nodos1[newC, newR])
          adjacencyList[nodos1[newC, newR]].add(nodos1[nodo[0], nodo[1]]) 

      adjacencyList[nodos1[nodo[0],nodo[1]]] = listaArestas
    
    return nodos1, adjacencyList


vizinhos = []

def caminha(u, E):
  global vizinhos
  u.distancia = 0
  u.ja_conheco = True
  vizinhos.append(u)
  while vizinhos:
    atual = vizinhos.pop(0)
    for v in E[atual]:
      if (v.ja_conheco == False) and v not in vizinhos:
        v.distancia = atual.distancia+1
        v.ja_conheco = True
        vizinhos.append(v)
      if v.coordenadas == endPos.coordenadas:
        print("distancia para chegar:", v.distancia) 
        return True

casos = ["caso100.txt", "caso150.txt", "caso200.txt", "caso250.txt", "caso300.txt", "caso350.txt", "caso400.txt", "caso450.txt", "caso500.txt", "caso550.txt"]

for caso in casos:
  print("caso:", caso)
  V, E = readG(caso)
  ts = time.time()
  caminha(knightPos, E)
  print("tempo do algoritmo de busca:", time.time() - ts)
  print("posição inicial: ")
  print(knightPos.coordenadas)
  print("posição final: ")
  print(endPos.coordenadas)
  print(len(E))
  print("\n")
  print("==============")
  print("\n")