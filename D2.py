#Verificar se o número digitado está ou não na sequencia de Fibonacci

def Sfibonacci(n):
    seq = [0, 1]
    
    while seq[-1] < n:
        prox = seq[-1] + seq[-2]
        seq.append(prox)
    
    return seq

def Emfibonacci(n):
    seq = Sfibonacci(n)
    
    if n in seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

#Entra com o número para execução

num = int(input("Informe um número: "))
resultado = Emfibonacci(num)
print(resultado)