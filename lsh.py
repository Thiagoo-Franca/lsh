import random
#variaveis globais

tabelaHashingBaldes = [[] for _ in range(101)]

vocabulario = {
    "aa": 0, "ab":1, "ac": 2, "ad": 3, "ae": 4, "af": 5,
    "ba": 6, "bb": 7, "bc": 8, "bd": 9, "be": 10, "bf": 11,
    "ca": 12, "cb": 13, "cc": 14, "cd": 15, "ce": 16, "cf": 17,
    "da": 18, "db": 19, "dc": 20, "dd": 21, "de": 22, "df": 23,
    "ea": 24, "eb": 25, "ec": 26, "ed": 27, "ee": 28, "ef": 29,
    "fa": 30, "fb": 31, "fc": 32, "fd": 33, "fe": 34, "ff": 35,
    }

n = len(vocabulario) 

#Shingles

def shingles (palavra):
    return (palavra[i:i+2] for i in range(len(palavra) - 1)) 

#Calcula a similaridade de Jaccard entre duas palavras
def calcular_jaccard(palavra1, palavra2):
    shingles1 = set(shingles(palavra1))
    shingles2 = set(shingles(palavra2))
    
    intersecao = shingles1 & shingles2
    uniao = shingles1 | shingles2
    
    similaridade = len(intersecao) / len(uniao)
    return similaridade


# Função para comparar todas as palavras em um balde usando a similaridade de Jaccard
def comparar_balde_lsh(balde):
    n = len(balde)
        
    if n == 1:
        print("O balde contém apenas uma palavra!")
        return
    
    for i in range(n):
        for j in range(i + 1, n):
            palavra1 = balde[i]
            palavra2 = balde[j]
            similaridade = calcular_jaccard(palavra1, palavra2)
            print(f"Similaridade entre '{palavra1}' e '{palavra2}': {similaridade:.2f}")

#Funcao Principal
def lsh(palavra):
    
    shingles_lista = []
    shingles_lista.append(shingles(palavra)) #[aa, ab, ba, ac, ca, aa, ac, ca, aa]

    #minHashing
    hash_bitmap = [0] * (n) 
    min_hash_bitmap = [0] * n
    assinatura = []

    for i in range(len(shingles_lista)):
        if (shingles_lista[i] in vocabulario):
            hash_bitmap[vocabulario[shingles_lista[i]]] = 1 #marcar na lista os shingles que estão presentes na palavra
            
    for k in range(len(hash_bitmap)):
        if hash_bitmap[k] == 1:
            min_hash_bitmap[(random.randint(0, 100)) * i % n] = 1 #gerar um valor aleatório para cada shingle presente na palavra
                
    menores = [float('inf')] * 30 #inicializa a lista de menores com infinito

    for i in range(len(min_hash_bitmap)):
        if min_hash_bitmap[i] == 1: 
            hashes = [(random.randrange(0, 100) * i) % n for _ in range(30)] #Gera funções aleatórias para cada shingle

            for j in range(30):
                if hashes[j] < menores[j]: #se o valor gerado for menor que o valor atual, substitui
                    menores[j] = hashes[j] 
    assinatura = menores

    #lsh

    bandas = []
    banda_size = 2  # Cada banda contém 2 valores da assinatura
    for i in range(0, len(assinatura), banda_size):
        bandas.append(assinatura[i:i + banda_size])

    hash_bandas = {(random.randint(0, 200)) % 101 for _ in range(len(bandas))}
    
    for hash_banda in hash_bandas:
        tabelaHashingBaldes[hash_banda].append(palavra)
    return    

#testes
lsh("abaaacadda")
lsh("ababbcadda")
lsh("babacbbaab")
lsh("bcbcacbcbb")
lsh("accdbbcdbc")
lsh("ddeeffabba")
lsh("bcbcbcbcdc")
lsh("acacacacac")
lsh("aaaeaaaffa")
lsh("ffabacbcbc")
lsh("abbadaccac")
lsh("acaddfdaca")
lsh("ababababab")
lsh("abbcbacbbd")
lsh("abadaffeae")
    
print(tabelaHashingBaldes)

# Testando a função com o balde específico
for i, balde in enumerate(tabelaHashingBaldes):
    if balde: 
        print(f"\nComparando palavras no balde {i}:")
        comparar_balde_lsh(balde)
