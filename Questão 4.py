class Pilha:
    def __init__(self):
        self.lista = []
    def push(self,valor):
        self.lista.append(valor)
        
    def pop(self):
        if (not(self.isEmpty())):
            self.lista.pop()
            
    def isEmpty(self):
        return len(self.lista) == 0
    
    def lenght(self):
        return len(lista.self)
    
    def peek(self):
        return self.lista[-1]

p = Pilha()

def pilha(p.lista):
    soma = 0
    for i in range(len(p.pilha)):
        p.pop()

        soma+= p.pilha


print(soma)
