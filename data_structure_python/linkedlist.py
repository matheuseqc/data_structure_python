
from node import Node
class LinkedList:   
    def __init__(self):
        self.head = None
        self.size = 0
           
    def append(self, elem, priority):
        novo_node = Node(elem, priority)
        if self.head is None:
            self.head = novo_node
            print(f'TAREFA {elem} ADICIONADA NA LISTA')
        elif self.head.priority < priority:
            novo_node.next = self.head
            self.head = novo_node
            print(f'TAREFA{elem} ADICIONADA DA LISTA ')
        else:
            current = self.head
            while current.next is not None and current.next.priority > priority:
                current = current.next
            if current.next is not None and current.next.priority == priority:
                print(f"JÁ EXISTE UM ELEMENTO COM A PRIORIDADE {priority}")
            else:
                novo_node.next = current.next
                current.next = novo_node
                print(f"TAREFA {elem} ADICIONADA NA LISTA")
        self.size += 1
    
    #len com lista encadeada contar elemento e atualizar elemento   
    def __len__(self):
         return self.size
    
    def get(self, index):
        pass
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
             if pointer:
                 pointer = pointer.next
             else:
                 print("list index out of range")
        if pointer:
            return pointer.data
        print("list index out of range")
    
    def set(self, index, elem):
        pass     
    
     
    def __setitem__(self, index,elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                print("ÍNDICE FORA DA LISTA")
        if pointer:
            pointer.data = elem
        else:
            print("ÍNDICE FORA DA LISTA")
    
    
    def get_priority(self, elem):
        pointer = self.head
        while pointer:
            if pointer.data == elem:
                return pointer.priority
            pointer = pointer.next
        print(f"ELEMENTO {elem} NÃO ENCONTRADO NA LISTA")
        return None
    
    
    def index(self, elem):
        #retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
               return i
            pointer = pointer.next
            i = i+1
        print(f'Elemento {elem} não está na lista')
    
    #remover elemento da lista encadeada
    def remover(self, elem):
        if self.head == None:
            print(" TAREFA {} NÃO ESTÁ NA LISTA ".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
            print(f"ELEMENTO {elem} EXCLUÍDO")
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.size = self.size - 1
                    print(f"ELEMENTO {elem}EXCLUÍDO")
                    return True
                ancestor = pointer
                pointer = pointer.next
        print("ELEMENTO NÃO ECONTRA-SE NA LISTA")





        
