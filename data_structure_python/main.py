from node import Node
from linkedlist import LinkedList
lista = LinkedList()
a = 0
while (a != 5):
    print("\n")
    a = int(input("ESCOLHA UM NÚMERO PARA MANIPULAR A LISTA:\n 1 - ADICIONAR NO FINAl \n 2 - EXCLUIR ELEMENTO \n 3 - ADICIONAR EM QUALQUER DA LISTA \n 4 - VER LISTA COMPLETA \n 5 - PEGAR O BECO:"))
    if (a == 1):
        b = int(input("QUAL ELEMENTO ADICIONAR?"))
        lista.append(b)
        print(f'ELEMENTO {b} ADICIONADO NO FINAL DA LISTA ')
         
    if (a == 2):
        c = int(input("QUAL ELEMENTO DESEJA EXCLUIR?"))
        lista.remover(5)
        print(f'ELEMENTO {c} EXCLUÍDO DA LISTA ')
    
    if (a == 3):
        d = int(input("QUAL ELEMENTO ADICIONAR?"))
        print(f'ELEMENTO {d} ADICIONADO NO FINAL DA LISTA ')
    
    if (a == 4):
        
        if (lista.size != 0):
            print("VALORES DA LISTA:")
            for i in range(len(lista)):
                print(lista[0+i])
        else:
            print("A LISTA ESTÁ VAZIA PARA VISUÁ-LA É NECESSÁRIO ADICIONAR VALOR NA LISTA")