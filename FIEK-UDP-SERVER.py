import socket
import math
import datetime
import string
import random
import numbers
import decimal
import itertools
import sys

serverPort=9000

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print ("Serveri eshte i gatshem per pranim te kerkesave ...")


while True:
        message,clientAddress=serverSocket.recvfrom(1024)
        message = message.decode("utf-8");
        ## Ketu shkruhen kushtet per mesazhin e pranuar 
        if message == "ip" or message == "IP":
            mesazhi = str(clientAddress).split("'")
            serverSocket.sendto(mesazhi[1].encode("utf-8"),clientAddress)
        elif message == "port" or message == "PORT":
             mesazhi = str(clientAddress).split(", ")
             mesazhi[1] = mesazhi[1][:len(mesazhi[1])-1]
             serverSocket.sendto(mesazhi[1].encode("utf-8"),clientAddress) 
        elif message.startswith("PRINTO ") or message.startswith("printo "):
            mesazhi=message[7:]
            if(mesazhi!=""):
               mesazhi = str(mesazhi)
               serverSocket.sendto(mesazhi.encode("utf-8"),clientAddress)
            else:
                serverSocket.sendto("Nuk keni shtypur fjalen!".encode("utf-8"),clientAddress)
        elif message.startswith("ZANORE ") or message.startswith("zanore "):
            mesazhi = message[7:]
            if(mesazhi!=""):
               zanore=list(str(mesazhi))
               count=0;
               for i in zanore:
                   if i in ["a","e","o","u","i","y","A","E","O","I","Y","U"]:
                       count+=1                      
               serverSocket.sendto(("Numri i zanoreve eshte " + str(count)).encode("utf-8"),clientAddress)
            else:
               serverSocket.sendto("Nuk keni shtypur tekst!".encode("utf-8"),clientAddress)
        elif message=="time" or message=="TIME":
              mesazhi=str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p"))
              serverSocket.sendto(mesazhi.encode("utf-8"),clientAddress) 
        elif message=="keno" or message=="KENO":
               serverSocket.sendto(str(random.sample(range(1, 81), 20)).encode("utf-8"),clientAddress) 
        elif message.startswith("FAKTORIEL ") or message.startswith("faktoriel "):
               mesazhi=message[10:]
               try:
                   numri = int(mesazhi)
                   faktorieli = 1
                   if numri < 0:
                      mesazhiModifikuar = "Faktorieli i numrave negativ nuk ekziston."
                   elif numri == 0:
                      mesazhiModifikuar = "Faktorieli i 0 eshte 1."
                   else:
                      for i in range(1,numri + 1):
                         faktorieli = faktorieli*i
                      mesazhiModifikuar = "Faktorieli i " + str(numri) + " eshte " + str(faktorieli)
                      #mesazhiModifikuar = str(faktorieli)
                   serverSocket.sendto(mesazhiModifikuar.encode("utf-8"),clientAddress)  
               except:
                   serverSocket.sendto("Ju lutem shkruani nje numer!".encode("utf-8"),clientAddress)
        elif message == "host" or message == "HOST":
             try:
                 mesazhi = socket.gethostbyaddr("localhost")
                 serverSocket.sendto(str(mesazhi).encode("utf-8"),clientAddress)
             except Exception:
                 serverSocket.sendto("Nuk lejohet kjo informate!",clientAddress)
        elif message.startswith("KONVERTO ") or message.startswith("konverto "):
            mesazhi = str(message).split(" ");
            if(mesazhi[1]!=""):
                try:
                    if(mesazhi[2]!=""):
                        if mesazhi[1].lower() == "celsiustokelvin":
                            temp = round(float(mesazhi[2])+273.15,2)
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "celsiustofahrenheit":
                            temp = round(float(mesazhi[2])*(9/5)+32,2)
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "kelvintofahrenheit":
                            temp = round(((float(mesazhi[2])-273.15)*(9/5)+32),2)
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "kelvintocelsius":
                            temp = round(float(mesazhi[2])-273.15,2);
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "fahrenheittocelsius":
                            temp = round((5/9)*(float(mesazhi[2])-32),2);
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "fahrenheittokelvin":
                            temp = round((5/9)*(float(mesazhi[2])-32)+273.15,2);
                            serverSocket.sendto(str(temp).encode("utf-8"),clientAddress)        
                        elif mesazhi[1].lower() == "poundtokilogram":
                            kilogram = round(float(mesazhi[2])/2.2,2)
                            serverSocket.sendto(str(kilogram).encode("utf-8"),clientAddress)
                        elif mesazhi[1].lower() == "kilogramtopound":
                            pound = round(float(mesazhi[2])*2.2,2)
                            serverSocket.sendto(str(pound).encode("utf-8"),clientAddress)
                        else:
                            serverSocket.sendto("Shtypni njerin nga opsionet!".encode("utf-8"),clientAddress)
                    else:
                          serverSocket.sendto("Shtypni numrin!".encode("utf-8"),clientAddress)
                except Exception:
                    serverSocket.sendto("Shtypni numrin!".encode("utf-8"),clientAddress)
            else:
                serverSocket.sendto("Shkruani njerin nga opsionet ne konvertim dhe numrin!".encode("utf-8"),clientAddress)
        elif message.startswith("enkripto ") or message.startswith("ENKRIPTO "):
                plaintext= str(message)[9:]
                if plaintext!="":
                        alfabeti = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                        qelesi = random.sample(range(1, 10), 3)
                        ciphertexti = ''
                        i=0
                        for c in plaintext:
                            if c in alfabeti:
                                ciphertexti += alfabeti[(alfabeti.index(c)+qelesi[i])%(len(alfabeti))]
                                i+=1
                                if i>2:
                                        i=0
                        serverSocket.sendto(str("MESAZHI I ENKRIPTUAR : "+ciphertexti).encode("utf-8"),clientAddress)
                else:
                        serverSocket.sendto(str("PlainTeksti nuk duhet te jete i zbrazet").encode("utf-8"),clientAddress)
        elif message.startswith("PRIME-SUM ") or  message.startswith("prime-sum "):
                 numrat=message[10:]
                 if(numrat!=""):
                     try:
                          numrat1=numrat.split(" ")
                          kufiri=int(numrat1[0])
                          ranngu=int(numrat1[1])
                     
                 
                          numbers=list(random.sample(range(1,kufiri),ranngu))        
                          i=2
                          sum=0
                          for c in numbers:
                              if(c==1 or c==2 or c==3):
                                  check=1
                                  sum=sum+c
                                  i=2
                              else:
                                  while i <= c/2:
                                   if c%i==0:
                                       check=0
                                       i=2
                                       break
                                   else:
                                       i+=1
                                       if c%i==0:
                                         check=0
                                         i=2
                                         break
                                       else:
                                           check=1
                                           sum=sum+c
                                           i=2
                                           break
                              
                          if(sum!=0):
                               msg="Shuma e numrave primar random eshte: " +str(sum)
                               serverSocket.sendto(msg.encode("utf-8"),clientAddress)
                     except:
                            serverSocket.sendto("Kufiri dhe rangu duhet te jene numra".encode("utf-8"),clientAddress)  
                 else:
                      exceptionMessage="Ju lutem deklaroni kufirin dhe rangun"
                      serverSocket.sendto(exceptionMessage.encode("utf-8"),clientAddress) 
        elif message.startswith("PIRAMIDA") or message.startswith("piramida"):
            numri = str(message).split(" ")
            try:
                numriRr = int(numri[1])
                if numriRr < 20:
                    k=int(0)
                    i=int(numriRr)
                    kastro = str("")
                    while i>0 :
                        j=int(1)
                        while j<i:
                            kastro = kastro+"   "
                            j=j+1
                        l=-k
                        while l<=k:
                            ndermjetesimi = str(abs(l)+1)
                            if (abs(l)+1) < 10:
                                kastro = kastro + ndermjetesimi+"  "
                            else:
                                kastro = kastro + ndermjetesimi+" "
                            l=l+1
                        serverSocket.sendto(kastro.encode("utf-8"),clientAddress)
                        kastro = ""
                        k=k+1
                        i=i-1
                    serverSocket.sendto("Perfundo".encode("utf-8"),clientAddress)
                else:
                    serverSocket.sendto("Permbajuni definimit te mesiperm!".encode("utf-8"),clientAddress)
            except Exception:  
                serverSocket.sendto("Permbajuni definimit te mesiperm!".encode("utf-8"),clientAddress)
        elif message.startswith("SHKRONJENUMERAPOKARAKTER") or message.startswith("shkronjenumerapokarakter"):
            shtypja = str(message).split(" ")
            if len(shtypja[1])==1:
                 if ord(shtypja[1])>=ord("A") and ord(shtypja[1])<=ord("Z"):
                     serverSocket.sendto(str("Shkronje e madhe!").encode("utf-8"),clientAddress)
                 elif ord(shtypja[1])>=ord("a") and ord(shtypja[1])<=ord("z"):
                     serverSocket.sendto(str("Shkronje e vogel!").encode("utf-8"),clientAddress)
                 elif ord(shtypja[1])>=ord("0") and ord(shtypja[1])<=ord("9"):
                     serverSocket.sendto(str("Numer!").encode("utf-8"),clientAddress)
                 else:
                     serverSocket.sendto(str("Karakter!").encode("utf-8"),clientAddress)
            else:
                    serverSocket.sendto(str("Gabim ne shtypje , shtyp vetem nje tast!").encode("utf-8"),clientAddress)     
        elif message.startswith("FIBONNACI ") or message.startswith("fibonnaci "):
               mesazhi = message[10:]
               try:

                    numri = int(mesazhi)
                    
                    if (numri > 0):
                       def fibonnaci(n):
                             if (n==1 or n==2):
                                 return 1
                             else:
                                 return fibonnaci(n-1) + fibonnaci(n-2)
                    
                       mesazhiModifikuar = []
                       for i in range(1,numri+1):
                           mesazhiModifikuar.append(fibonnaci(i))
                    
                       serverSocket.sendto(str(mesazhiModifikuar).encode("utf-8"),clientAddress)
                    
                    else:
                       serverSocket.sendto("Nuk mund te kthehet seria me numer negativ te anetareve !".encode("utf-8"),clientAddress)
               except:
                    serverSocket.sendto("Ju lutem shkruani nje numer !".encode("utf-8"),clientAddress)
        elif message.startswith("ROOT ") or message.startswith("root "):
           mesazhi = message[5:]
           if(mesazhi!=""):
                ip = socket.gethostbyname( mesazhi )
                try:
                   host = socket.gethostbyaddr( ip )
                   hostname = str(host).split("'")
                   if(mesazhi == hostname[1]):
                       serverSocket.sendto(("Pergjigjet qe kthehen nga " +str(mesazhi) + " jane autoritative ! \n" +
                                            "Emri : " + str(mesazhi) + "\n" +
                                            "Adresa : " + str(ip) + "\n" + 
                                            "Emri i hostit : " + str(hostname[1]) + "\n" +
                                            "Hosti : " + str(host)).encode("utf-8"),clientAddress)
                   else:
                       serverSocket.sendto(("Pergjigjet qe kthehen nga " + str(mesazhi) + " nuk jane autoritative ! \n" +
                                            "Emri : " + str(mesazhi) + "\n" +
                                            "Adresa : " + str(ip) + "\n" + 
                                            "Emri i hostit : " + str(hostname[1]) + "\n" +
                                            "Hosti : " + str(host)).encode("utf-8"),clientAddress)
                
                except:
                    serverSocket.sendto(("Pergjigjet qe kthehen nga " + str(mesazhi) + " nuk jane autoritative ! \n" +
                                            "Emri : " + str(mesazhi) + "\n" +
                                         "Adresa : " + str(ip) + "\n" + 
                                         "Emri i hostit : Nuk mund te kthehet !").encode("utf-8"),clientAddress)
           else :
               serverSocket.sendto(("Ju lutem shkruani nje link !").encode("utf-8"),clientAddress)
        elif message.startswith("KOMBINIMET ") or message.startswith("kombinimet "):
                l = str(message[11:])
                if (l!=""):
                    comb = []
                    for i in range(len(l)):
                      comb += itertools.combinations(l,i+1)
                    serverSocket.sendto((("Kombinimet  e mundshme janë: " )+str(comb)).encode("utf-8"),clientAddress)
                else:
                   serverSocket.sendto(("Ju lutem plotesoni fushen e kerkuar!" ).encode("utf-8"),clientAddress)
        elif message.startswith("VITI ") or message.startswith("viti "):
              try: 
                vitiilindjes=int(message[5:])
               
                viti = int(datetime.datetime.now().strftime("%Y"))
                mosha = viti-vitiilindjes   
                if mosha<1 :  
                   serverSocket.sendto(("Mosha nuk mund te shfaqet!" ).encode("utf-8"),clientAddress)
                else  :
                   serverSocket.sendto(("Mosha e personit është: " + str(mosha)).encode("utf-8"),clientAddress)
              except:
                   serverSocket.sendto(("Ju lutem shkruani vitin e lindjes!" ).encode("utf-8"),clientAddress) 
        elif message.startswith("SHENDRRO") or message.startswith("shendrro"):
              message = message.split(" ")
              if message[1]!="":
                    if message[2]!="":
                        if message[1].lower() == "dectobin":
                            numri = bin(int(message[2]))[2:]
                            serverSocket.sendto(("Numri binar eshte : " + str(numri)).encode("utf-8"),clientAddress)
                        elif message[1].lower() == "dectooct":
                            numri = oct(int(message[2]))[2:]
                            serverSocket.sendto(("Numri oktal eshte : " + str(numri)).encode("utf-8"),clientAddress)
                        elif message[1].lower() == "dectohex":
                            numri = hex(int(message[2]))[2:]
                            serverSocket.sendto(("Numri heksadecimal eshte : " + str(numri)).encode("utf-8"),clientAddress)
                        elif message[1].lower() == "hextodec":
                            numri = int(message[2], 16)
                            serverSocket.sendto(("Numri decimal eshte : " + str(numri)).encode("utf-8"),clientAddress)
                        elif message[1].lower() == "octtodec":
                            numri = int(message[2], 8)
                            serverSocket.sendto(("Numri decimal eshte : " + str(numri)).encode("utf-8"),clientAddress)
                        elif message[1].lower() == "bintodec":
                            numri = int(message[2], 2)
                            serverSocket.sendto(("Numri decimal eshte : " + str(numri)).encode("utf-8"),clientAddress)
                    else:
                         serverSocket.sendto(("Ju lutem shkruani numrin e deshiruar").encode("utf-8"),clientAddress)
              else:
                   serverSocket.sendto(("Ju lutem shkuani opcionin dhe numrin e deshiruar").encode("utf-8"),clientAddress)
        elif message.startswith("LEAPYEAR") or message.startswith("leapyear"):
              mesazhi = str(message)[8:]
              if mesazhi!="":
                viti = int(mesazhi)
                if (viti % 4 == 0 and viti % 100 != 0) or (viti % 400 == 0):
                    serverSocket.sendto((str(viti)+ " eshte vit i brishte").encode("utf-8"),clientAddress)
                else:
                    serverSocket.sendto((str(viti)+ " nuk eshte vit i brishte").encode("utf-8"),clientAddress)
              else:
                  serverSocket.sendto(("Ju lutem shkruani vitin e deshiruar").encode("utf-8"),clientAddress)                    
        else:
            serverSocket.sendto("ERROR".encode("utf-8"),clientAddress) 
