class Stack:
  def __init__(self):
    self.lista = []
  def push(self,valor):
    self.lista.append(valor)
    print("Sua Pilha Agora é: ",self.lista)
        
  def pop(self):
    if (not(self.isEmpty())):
      self.lista.pop()
            
  def isEmpty(self):
    return len(self.lista) == 0
    
  def lenght(self):
    return len(self.lista)
    
  def peek(self):
    return self.lista[-1]

#Letra A 
print("Letra A")
print("\n")
  

stack = Stack()
for i in range(16) :
  if i % 3 == 0 :
    stack.push(i)

print("\n")

#Letra B
print("Letra B")
print("\n")

stack = Stack()
for i in range( 16 ) :
  if i % 3 == 0 :
    stack.push( i )
  elif i % 4 == 0 :
    stack.pop()
