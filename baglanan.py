import socket
import os
os.system("color c")
os.system("cls")
print(""" 

                                                                                                              
      ##      ###   ###                          #######                 /         /                        
     /####       ###   ###                       /       ###             #/        #/                         
    /  ###        ##    ##                      /         ##             ##        ##                   #     
       /##        ##    ##                      ##        #              ##        ##                  ##     
      /  ##       ##    ##                       ###                     ##        ##                  ##     
      /  ##       ##    ##  ##   ####           ## ###           /###    ##  /##   ## /###     /##   ######## 
     /    ##      ##    ##   ##    ###  /        ### ###        / ###  / ## / ###  ##/ ###  / / ### ########  
     /    ##      ##    ##   ##     ###/           ### ###     /   ###/  ##/   ### ##   ###/ /   ###   ##     
    /      ##     ##    ##   ##      ##              ### /##  ##    ##   ##     ## ##    ## ##    ###  ##     
    /########     ##    ##   ##      ##                #/ /## ##    ##   ##     ## ##    ## ########   ##     
   /        ##    ##    ##   ##      ##                 #/ ## ##    ##   ##     ## ##    ## #######    ##     
   #        ##    ##    ##   ##      ##                  # /  ##    ##   ##     ## ##    ## ##         ##     
  /####      ##   ##    ##   ##      ##        /##        /   ##    ##   ##     ## ##    /# ####    /  ##     
 /   ####    ## / ### / ### / #########       /  ########/     ######    ##     ##  ####/    ######/   ##     
/     ##      #/   ##/   ##/    #### ###   m /     #####        ####      ##    ##   ###      #####     ##    
#                                     ###  i |                                  /                             
 ##                            #####   ### n  \)                               /                              
                             /#######  /#  u                                  /                               
                            /      ###/    s                                 /       

[!] Uyarı Türkçe ifadeler girilmez mesela; ş,İ,ö,ü,ç gibi [!]

!Bu program @alismsk234 tarafından kodlanmıştır!

(Azerbaycan-Türkiye)

C = çık
""")
ad = input("Kullanıcı adın nedir>> ")
soket = socket.socket()
host = input("Ngrok link gir>> ")
port = int(input("Ngrok port gir>> "))
soket.connect((host,port))
while True:
    data = str(soket.recv(1024))[1:]
    if data:
        print("Karsi taraf: {}".format(data))
        respond = input(ad+": ").encode("utf-8")
        if respond == b"C":
            exit()
        else:
            soket.sendall(bytes(respond))