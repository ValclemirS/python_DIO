N = int(input())

while N > 0:
    entrada= input().split()
    A,B=entrada[0],entrada[1]
    if A.endswith(B):
        print("encaixa")
    else:
         print("nao encaixa")
    N -= 1

