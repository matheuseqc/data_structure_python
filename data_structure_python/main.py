from node import Node
from linkedlist import LinkedList
lista = LinkedList()
a = 0
while (a != 5):
    print("\n")
    a = int(input("ESCOLHA UM NÚMERO PARA MANIPULAR A LISTA:\n 1 - ADICIONAR NO FINAl \n 2 - EXCLUIR ELEMENTO \n 3 - ADICIONAR EM QUALQUER DA LISTA \n 4 - VISUALIZAÇÃO DA LISTA \n 5 - SAIR:"))
    if (a == 1):
        b = int(input("QUAL ELEMENTO ADICIONAR?"))
        lista.append(b)
        print(f'ELEMENTO {b} ADICIONADO NO FINAL DA LISTA ')
        while True:
            ped = int(input("DESEJA CONTINUAR A ADICIONAR ELEMENTO NO FINAL? \n 1- SIM \n 2- NÃO:"))
            if (ped == 1):
                b = int(input("QUAL ELEMENTO ADICIONAR:"))
                lista.append(b)
                print(f'ELEMENTO ADICIONADO {b} NO FINAL DA LISTA')
            if (ped != 2 and ped !=1):
              print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
            if (ped == 2):
                break
             
    if (a == 2):
        if (lista.size != 0):
            c = int(input("QUAL ELEMENTO DESEJA EXCLUIR?"))    
            lista.remover(c)
            print(f'ELEMENTO {c} EXCLUÍDO DA LISTA ')
            while True:
                ex = int(input("DESEJA CONTINUAR A EXCLUIR? \n 1- SIM \n 2- NÃO:"))
                if (ex == 1):
                    c = int(input("QUAL ELEMENTO EXCLUIR:"))
                    lista.remover(c)
                    print(f'ELEMENTO {c} EXCLUÍDO DA LISTA')
                if (ex != 2 and ex !=1):
                    print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
                if (ex == 2):
                    break
        else:
            print("A LISTA ENCONTRA-SE VAZIA NÃO HÁ COMO REMOVER") 
                 
    if (a == 3):
        position = int(input("POSIÇÃO QUE DESEJA ADICIONAR ESSE ELEMENTO:"))
        elemento = int(input("QUAL ELEMENTO COLOCAR NESSA POSIÇÃO:"))
        if (position <= lista.size):
            lista.insert(position, elemento)
            print(f'ELEMENTO {elemento} ADICIONADO NA POSIÇÃO {position}')
            while True:
                sn = int(input("DESEJA CONTINUAR A ADICIONAR ELEMENTO? \n 1- SIM \n 2- NÃO:"))
                if (sn == 1):
                    pos = int(input("POSIÇÃO QUE DESEJA ADCIONAR ESSE ELEMENTO:"))
                    elemen = int(input("QUAL ELEMENTO COLOCAR NESSA POSIÇÃO:"))
                    if (pos <= lista.size):
                        lista.insert(pos, elemen)
                        print(f'ELEMENTO {elemen} ADICIONADO NA POSIÇÃO {pos}')
                    else:
                        print("POSIÇÃO MAIOR QUE O DA LISTA")
                if (sn != 2 and sn !=1):
                    print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
                if (sn == 2):
                    break 
        else:
            print("POSIÇÃO MAIOR QUE O DA LISTA")   
    if (a == 4):
        if (lista.size != 0):
            print("VALORES DA LISTA:")
            for i in range(len(lista)):
                print(lista[0+i])
        else:
            print("A LISTA ESTÁ VAZIA PARA VISUÁ-LA É NECESSÁRIO ADICIONAR VALOR NA LISTA")