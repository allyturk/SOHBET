import socket 
import os
os.system("color c")
os.system("cls")
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(""" 

                                                                                                              
       ##      ###   ###                           #######                 /         /                        
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
host = input("127.0.0.1 yaz>> ")
port = int(input("ngrok başlattığında portu gir>> "))
soket.bind((host,port))
kackisi = int(input("En fazla kaç kişi bağlanacak>> "))
soket.listen(kackisi)
c,addr = soket.accept()
c.sendall(bytes("Hos gelmissin!".encode("utf-8")))
print("{} bağlandı.".format(addr))
while(True):
    data = str(c.recv(1024))[1:]
    if data:
        print("Karsi taraf: {}".format(data))
        
        respond = input(ad+": ").encode("utf-8")
        if respond == b"C":
            exit()
       

        else:  
            c.sendall(bytes(respond))