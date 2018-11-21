class Pilha:
    def __init__(self):
        self.pilha = []
        self.soma = 0 
        
    def push(self,valor):
        self.pilha.append(valor)
        
    def pop(self):
        if (not(self.isEmpty())):
            self.pilha.pop()
            
    def isEmpty(self):
        return len(self.pilha) == 0
    
    def lenght(self):
        return len(pilha.self)
    
    def peek(self):
        return self.pilha[-1]
    
    def stack(self):
        lista = []
        for i in range(len(self.pilha)):
            lista.append(self.pilha[i])
        for i in lista:
            self.soma +=i
        print("Desempilhada: ",lista)
        print("Soma: %d"%(self.soma))

p = Pilha()
p.push(1)
p.push(2)
p.stack()
