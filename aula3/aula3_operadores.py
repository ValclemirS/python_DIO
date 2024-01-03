x=1;
y=2;
z=3;
t=True;
soma= x+y;
subtracao=x-y;
divisao=y/x;
multiplicacao=z*y;
modulo=z%y;
exponciacao=y**z;
print(soma,subtracao,divisao,multiplicacao,modulo,exponciacao, sep='\n', end="\n----\n");
maior=x>y;
menor=x<y;
maior_ou_igual=z>=y;
menor_ou_igual=y<=y;
diferente=x!=y;
igual=x==z;
print(maior,maior_ou_igual,menor_ou_igual,diferente,igual,sep='\n',end="\n----\n")
def sacar(valor):
    print(valor)
sacar(10) 

if(x>y or z>y): # || o operador ou
    print("ok")
if(x<y and y<z): # & o operador e
    print("ok ok")
print(not t)#  o operador not

print(x is y)# o operador is é para verificar se a variavel x ocupa o mesmo espaço de memoria que y
print(x is not y)# o operador is not é para verificar se a variavel x nao ocupa o mesmo espaço de memoria que y
