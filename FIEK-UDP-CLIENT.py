from socket import *
import sys

serverAddress = "localhost"
serverPort = 9000

clientSocket = socket(AF_INET, SOCK_DGRAM)

print ("Shtyp:\n")
print ("IP - Per ti shfaqur IP e juaja\nPORT - Per t'a shfaqur numrin e portit tuaj\nZANORE (nje tekst nga ana juaj) - Per te shfaqur numrin e zanoreve ne ate tekst")
print("PRINTO (nje tekst nga ana juaj) - Per t'a kthyer mbrapa tekstin e dhene nga ju\nHOST - Per te shfaqur emrin e serverit ku eshte hostuar klienti")
print("TIME - Per te kthyer kohen reale (real-time)\nKENO - Kthen 20 numra te rastesishem nga rangu 1-80\nFAKTORIEL (numri i juaj) - Gjen faktorielin si rezultat i parametrit te dhene hyres")
print("KONVERTO (opcioni {hapsire} numri i deshiruar)\n")
print("Kthen si rezultat konvertimin e opcioneve varesisht opcionit te zgjedhur\n"
+"Lista e parametrave opcioni jane:\n"
+"CelsiusToKelvin\n"
+"CelsiusToFahrenheit\n"
+"KelvinToFahrenheit\n"
+"KelvinToCelsius      \n"
+"FahrenheitToCelsius  \n"
+"FahrenheitToKelvin   \n"
+"PoundToKilogram      \n"
+"KilogramToPound      \n"
)
#implementimi i metodave personale - AGONI
print("SHENDRRO (opcioni {hapsire} numri i deshiruar)\nKthen si rezultat shendrrimin e numrave varesisht nga opcioni i zgjedhur\n"
        +"Lista e parametrave te opcionit jane:\n"
        +"DecToBin \nDecToOct \nDecToHex \nBinToDec \nOctToDec \nHexToDec \n")
print("LEAPYEAR (viti) - Kthen mesazhin se a eshte viti i brishte")
#implementimi i metodave personale - ERUDITI
print("FIBONNACI (opcioni {hapsire} numri i deshiruar) - Kthen si rezultat serine e numrave Fibonnaci \nme aq anetar sa opcioni i zgjedhur")
print("ROOT (opcioni {hapsire} nje link) - Tregon nese linku i zgjedhur eshte root server apo jo ")
#implementimi i metodave personale - DRITONI
print("KOMBINIMET (opcioni {hapsire} teksti i deshiruar) - Kthen si rezultat te gjitha kombinimet e opcionit te zgjedhur")
print("VITI (opcioni {hapsire} viti i lindjes ) - Kthen si rezultat moshen ")
#implementimi i metodave personale - BETIMI
print("ENKRIPTO {plaintext} kthen tekstin e enkriptuar me Algoritmin e Vigenerit")
print("PRIME-SUM {kufiri i random-generator} {gjatesia e listes se numrave } - Kthen shumen e numrave primar te gjeneruar rastesisht")
#implementimi i metodave personale - KASTRIOTI
print("PIRAMIDA {hapsire} (int) - Kthen numrin e dhene ne rreshta te piramides!")
print("SHKRONJENUMERAPOKARAKTER (shtyp nje tast te tastieres) - Tregon cfare tasti eshte!")

message = input("Shkruaj komanden: ")
clientSocket.sendto(message.encode("utf-8"),(serverAddress,serverPort))

while True:
    
    modifiedMessage = clientSocket.recv(1024)
    if message.startswith("PIRAMIDA") or message.startswith("piramida"):
         if modifiedMessage.decode("utf-8") != "Perfundo" and modifiedMessage.decode("utf-8") != "Permbajuni definimit te mesiperm!":
             print (modifiedMessage.decode("utf-8"))
         elif modifiedMessage.decode("utf-8") == "Permbajuni definimit te mesiperm!":
             print (modifiedMessage.decode("utf-8"))
             break 
         else:
             break
    else:
         print (modifiedMessage.decode("utf-8"))
         break   
clientSocket.close()
