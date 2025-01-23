import csv


print ("="*50)
print ("Seja bem vindo a *BIBLIOTECA MASTER*".center(50))
print ("="*50)

'''
#`listar_livros_por_autor(dicionario, autor)`: Retorna uma lista de títulos de livros de um determinado autor.
def listar_livros_por_autor(dicionario, autor):
    chaves = [] 
    resultados = [] 
    for i in dicionario: 
        if dicionario[i][1] == autor: 
            chaves.append(i)

    for e in chaves: 
        resultados.append(dicionario[e]) 
    for resultado in resultados: 
        print(resultado) 
    return resultados



#- `listar_livros_por_genero(dicionario, genero)`: Retorna uma lista de títulos de livros de um determinado gênero.
def listar_livros_por_genero(dicionario, genero):
    chaves = [] 
    resultados = [] 

    for i in dicionario: 
        if dicionario[i][2] == genero: 
            chaves.append(i)

    for e in chaves: 
        resultados.append(dicionario[e]) 
    for resultado in resultados: 
        print(resultado) 
'''

#- `adicionar_livro(dicionario, id_livro, titulo, autor, genero)`: Adiciona um livro ao dicionário e atualiza os conjuntos de autores e gêneros.
def adicionar_livro(dicionario, titulo, autor, genero):
    
    lista_key = []
    for i in dicionario:
        lista_key.append(i)
    
    id_livro = lista_key[-1] + 1

    valor = titulo, autor, genero

    dicionario[id_livro] = tuple(valor)
    
    print (f"o livro {dicionario[id_livro] [0]} foi adicionado com sucesso!!" )


    return (dicionario)




#PASSO 1: LER O ARQUIVO
#criando as listas para processar o arquivo csv
chave = []

valor =[]

#lendo o arquivo csv
with open (r'project biblioteca\biblioteca.csv', "r", encoding="utf-8", ) as f:
    biblioteca_lida = csv.DictReader(f)# não é necessário definir o fieldname pois ele automaticamente é definido pela primeira linha do arquivo
    for reader in biblioteca_lida:
    
        chave.append(int(reader['id'])) #redefinindo as keys do dicionario

        valorx = (reader['titulo'], reader['autor'], reader['genero']) #redefinindo os valores do dicionario

        valor.append(valorx)
    
#recriando o dicionario apartir do arquivo csv
biblioteca = dict(zip(chave, valor))



#2 PASSO: PERGUNTAR QUAL OPERAÇÃO O USUARIO DESEJA REALIZAR
oper = str(input("Bem vindo ao gerenciador de livros!!\ntemos as seguintes opçoes:\n consultar os autores para isso tecle 1 \n consultar os generos disponiveis para isso tecle 2\n consultar os livros disponiveis 3 \n adicionar livro 4 \n remover livro 5 \n o que deseja fazer: "))


# retorna a lista de autores
if oper == "1":
    lista_autores = []

    for l in biblioteca:
        lista_autores.append (biblioteca[l][1])
    lista_autores = set (lista_autores)
    for b in lista_autores:
        print(b)
# retorna todos os generos disponiveis
elif oper == "2":
    lista_genero = []

    for l in biblioteca:
        lista_genero.append(biblioteca[l][2])
    lista_genero = set(lista_genero)
    for b in lista_genero:
        print(b)
# retorna os livros disponiveis 
elif oper == "3":
    for i in biblioteca:
        print (biblioteca[i][0])
# faz a implementação de um livro
elif oper == "4":
    titulo = input("qual é o titulo do livro: ")
    autor = input("qual é o autor do livro: ")
    genero = input("qual é o genero do livro: ")
    
    adicionar_livro(biblioteca, titulo, autor, genero)


    lista_livros = [{"id": id, "titulo": titulo, "autor": autor, "genero": genero} for id, (titulo, autor, genero) in biblioteca.items()]


    #adicionando o livro ao arquivo csv
    with open(r'project biblioteca\biblioteca.csv', mode='w', encoding='utf-8', newline='') as f:
        fieldnames = ["id", "titulo", "autor", "genero"] #definindo as chaves do arquivo 
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()#escrevendo as chaves do arquivo no cabeçalho
        writer.writerows(lista_livros)
elif oper == "5":
    nome_livro = (input("qual o nome do livro a ser deletado: "))
    
    x = 1
    
    lista_titulo = []

    for l in biblioteca:
        lista_titulo.append (biblioteca[l][0])

    for i in lista_titulo:

        if i == nome_livro:
            del biblioteca[x]
            lista_livros = [{"id": id, "titulo": titulo, "autor": autor, "genero": genero} for id, (titulo, autor, genero) in biblioteca.items()]


            #reescrevendo o arquivo para alterar remover o livro selecionado
            with open(r'project biblioteca\biblioteca.csv', mode='w', encoding='utf-8', newline='') as f:
                fieldnames = ["id", "titulo", "autor", "genero"] #definindo as chaves do arquivo 
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()#escrevendo as chaves do arquivo no cabeçalho
                writer.writerows(lista_livros)
            
            print(f"o livro {nome_livro} foi deletado com sucesso")

        elif oper != nome_livro:
            x += 1
            if x > chave[-1]:
                print("você digitou o nome errado tente denovo")


