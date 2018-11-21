class Pilha():
    def __init__(self):
        self.lista = []
        self.valorMaximo = 0 
    def push(self,valor):
        if len(self.lista) == 10:
            print("A lista atingiu o valor maximo")
            self.valorMaximo = 1
                
        if self.valorMaximo == 0:
            self.lista.append(valor)
        self.valorMaximo = 0
             
    def pop(self):
        if (not(self.isEmpty())):
            self.lista.pop()
            
    def isEmpty(self):
        return len(self.lista) == 0
    
    def lenght(self):
        return len(lista.self)
    
    def peek(self):
        return self.lista[-1]


pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
pilha.push(3)
print(pilha.lista)
