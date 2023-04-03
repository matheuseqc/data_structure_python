
from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    #adiciona Elemento no final da lista    
    def append(self, elem):
        if self.head:
            #adiciona quando já tem elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
                
            #último valor vazio
            pointer.next = Node(elem)
        else:
            # primero nó adicionado 
            self.head = Node(elem)
        self.size +=1
    
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
                 raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def set(self, index, elem):
        pass     
    
     
    def __setitem__(self, index,elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                print("Índice fora da lista")
        if pointer:
            pointer.data = elem
        else:
            print("Índice fora da lista")
    
    def index(self, elem):
        #retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
               return i
            pointer = pointer.next
            i = i+1
        raise ValueError(f'Elemento {elem} não está na lista')
    
    
    #inserir em uma posição qualquer da lista
    def insert(self, index, elem):
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node     
        if index == 0 and self.size:
            pointer = self.head
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next
                else: 
                    raise IndexError("Posição maior que o da lista")
            self.size +=1
        else:
            pointer = self.head
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next
                else: 
                    raise IndexError("Posição maior que o da lista")
            self.size +=1  
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node

    #remover elemento da lista encadeada
    def remover(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
            print("ELEMENTO EXCLUÍDO")
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.size = self.size - 1
                    print("ELEMENTO EXCLUÍDO")
                    return True
                ancestor = pointer
                pointer = pointer.next
        print("ELEMENTO NÃO ECONTRA-SE NA LISTA")





        
