#JOAO ICARO MOREIRA LOIOLA -> 537176
#MARIA JULIA SIQUEIRA -> 541577
#MARIA EDUARDA NOGUEIRA FREITAS -> 536868
#YLANA MARIA ARAUJO TORRES -> 541566

import networkx as nx
import matplotlib.pyplot as plt

arquivo = "./G1.txt"
fig, ax = plt.subplots()

def plotar(vertices, arestas, cores):

    ax.clear()

    GRAFO = nx.DiGraph()
    GRAFO.add_nodes_from(vertices)
    GRAFO.add_edges_from(arestas)

    posicoes = nx.circular_layout(GRAFO)
    nx.draw(GRAFO, posicoes, with_labels =True, font_weight="bold", node_size=700, font_size= 20, font_color="red", arrowsize=15, node_color="red")

    for i in cores:
        visited[i] = ""
        cor = "white"
        if cores[i] == "cinza":
            cor = "gray"
        elif cores[i] == "preto":
            cor = "black"
       
        nx.draw_networkx_labels(
            GRAFO,
            pos=posicoes,
            labels=visited,
            font_size=12,
            font_color="black",
            font_weight="normal",
        )
        nx.draw_networkx_nodes(
            GRAFO,
            pos=posicoes,
            nodelist=[i],
            label=i,
            node_color=cor,
            cmap=plt.cm.Blues,
            node_size=800,
            edgecolors= "blue" if cor == "white" else None if cor == "black" else "black",
        )

    plt.show(block=False)
    plt.pause(0.2)
    if all(cor == "preto" for cor in cores.values()) and cores != {}:
        plt.pause(20)
        plt.close()

#função que recebe um grafo como parametro 
def DFS(grafo):
    global cor, d, f, tipo_aresta, vm #inicializando váriaveis globais 
    cor, d, f, tipo_aresta, vm = {}, {}, {}, [], 0
    
    vertices = sorted(grafo, key=lambda v: len(grafo[v]), reverse=True)

    for u in vertices:
        plotar(vertices_arquivo, arestas_arquivo, cor)
        cor[u] = "branco"
        plotar(vertices_arquivo, arestas_arquivo, cor)

    for u in vertices:
        if cor.get(u) == 'branco':
            DFS_VISIT(grafo, u)

#função que recebe o grafo e um vertice como parametro 
def DFS_VISIT(grafo, u):
    global cor, d, f, tipo_aresta, vm
    plotar(vertices_arquivo, arestas_arquivo, cor) # ICARO 
    cor[u] = 'cinza'
    plotar(vertices_arquivo, arestas_arquivo, cor) # ICARO 
    vm += 1
    d[u] = vm

#se o vertice igual a branco chamar a função visit e usando o append para inserir no final da lista
    for v in grafo[u]:
        if cor.get(v) == 'branco':
            tipo_aresta.append(f"Aresta ({u}, {v}): Árvore")
            DFS_VISIT(grafo, v)
        elif d[u] < d.get(v, 0):
            tipo_aresta.append(f"Aresta ({u}, {v}): Avanço")
        elif cor.get(v) == 'cinza':
            tipo_aresta.append(f"Aresta ({u}, {v}): Retorno")
        else:
            tipo_aresta.append(f"Aresta ({u}, {v}): Cruzamento")

    plotar(vertices_arquivo, arestas_arquivo, cor) # ICARO 
    cor[u] = 'preto'
    plotar(vertices_arquivo, arestas_arquivo, cor) #ICARO
    vm += 1
    f[u] = vm

def ler_grafo_do_arquivo(arq): #função para a leitura do arquivo que contém o grafo
    vertices = set()
    arestas = []
    grafo = {}

    with open(arq, 'r') as arquivo:
        info = arquivo.readline().split()  #lê a primeira linha que contém as informações sobre o grafo(vertices, arestas
        # e se é grafo ou digrafo)

        if len(info) < 3:   #verifica se tem as três informações sobre o grafo
            print("Formato inválido da primeira linha.")
            return vertices, arestas

        num_vertices, num_arestas, tipo_grafo = int(info[0]), int(info[1]), info[2]

        for _ in range(num_arestas): #leitura das arestas 
            linha = arquivo.readline().split()

            if len(linha) == 2: #verfica se tem os dois vertices na
                u, v = (linha[0], linha[1])
                vertices.add(u) #adiciona vértices à lista
                vertices.add(v)

                #CRIAR LISTA DE ADJ
                if u not in grafo:
                    grafo[u] = []

                arestas.append((u, v)) #adciona a aresta que liga esses dois vértices à lista
                grafo[u].append(v)
            else:
                print("Formato inválido em uma linha de aresta. Ignorando.")
    print(grafo)
    return list(vertices), arestas, grafo

vertices_arquivo, arestas_arquivo, grafo = ler_grafo_do_arquivo(arquivo)
visited = {i: "/" for i in grafo}

DFS(grafo)

print("Valores do vetor d:", d)
print("Valores do vetor f:", f)
print("Nomenclatura das arestas:")

for aresta in tipo_aresta:
    print(aresta)