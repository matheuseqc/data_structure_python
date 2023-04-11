from node import Node
from linkedlist import LinkedList
lista = LinkedList()
a = 0
while (a != 5):
    print("\n")
    a = int(input("ADICIONE UM AFAZER:\n 1 - ADICIONAR TAREFA\n 2 - EXCLUIR TAREFA \n 3 - ATUALIZAR VALOR DA LISTA\n 4 - VISUALIZAÇÃO DA LISTA\n 5 - SAIR:"))
    if (a == 1):
        b = input("QUAL TAREFA DESEJA ADICIONAR?")
        p = int(input("QUAL A PRIORIDADE: "))
        index = lista.size
        lista.append(b,p)
        while True:
            ped = int(input("DESEJA CONTINUAR A ADICIONAR TAREFA? \n 1- SIM \n 2- NÃO:"))
            if (ped == 1):
                b = input("QUAL TAREFA ADICIONAR:")
                p = int(input("QUAL A PRIORIDADE: "))
                lista.append(b,p)
                tam = lista.size
                if(lista.size > tam):
                    print(f'TARFA {b} ADICIONADA DA LISTA ')
            if (ped != 2 and ped !=1):
              print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
            if (ped == 2):
                break
             
    if (a == 2):
        if (lista.size != 0):
            c = input("QUAL ELEMENTO DESEJA EXCLUIR?")    
            lista.remover(c)
            while True:
                ex = int(input("DESEJA CONTINUAR A EXCLUIR? \n 1- SIM \n 2- NÃO:"))
                if (ex == 1):
                    c = input("QUAL ELEMENTO EXCLUIR:")
                    lista.remover(c)
                if (ex != 2 and ex !=1):
                    print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
                if (ex == 2):
                    break
        else:
            print("A LISTA ENCONTRA-SE VAZIA NÃO HÁ COMO REMOVER") 
        
    if (a == 3):
        indice = int(input("QUAL A POSIÇÃO QUE DESEJA ATUALIZAR O AFAZER:"))
        addelement = input("QUAL O VALOR ATUALIZADO:")
        if (indice <= lista.size):
            lista.__setitem__(indice-1, addelement)
            print(f'TAREFA {addelement} ATUALIZADA NA POSIÇÃO {indice }')
            while True:
                sup = int(input("DESEJA CONTINUAR A ATUALIZAR TAREFA? \n 1- SIM \n 2- NÃO:"))
                if (sup == 1):
                    indice1 = int(input("QUAL A POSIÇÃO QUE DESEJA ATUALIZAR A TAREFA:"))
                    addelement1 = input("QUAL A TAREFA ATUALIZADA:")
                    if (indice1<= lista.size):
                        lista.__setitem__(indice1, addelement1)
                        print(f'TAREFA {addelement1} ATUALIZADA NA POSIÇÃO {indice1}')
                    else:
                        print("ÍNDICE FORA DA LISTA")
                if (sup != 2 and sup !=1):
                    print("VALOR FORA DA LISTA DIGITE UM OU DOIS.")  
                if (sup == 2):
                    break 
        else:
            print("ÍNDICE FORA DA LISTA")                    
    if (a == 4):
        if (lista.size != 0):
            print("LISTA DE AFAZERES DE ACORDO COM A PRIORIDADE:")
            for i in range(len(lista)):
                print(lista.get_priority(lista[0+i]) , "-" ,lista[0+i])
        else:
            print("A LISTA ESTÁ VAZIA PARA VISUÁ-LA É NECESSÁRIO ADICIONAR VALOR NA LISTA")