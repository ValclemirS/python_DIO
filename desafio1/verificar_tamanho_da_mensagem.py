b="passou"
a="aprovou"
T = input("digite sua mensagem: ")

if len(T)<140:
    print(a.upper().center(10,"#"))
else :
    print(b)