import os
import time
from bs4 import BeautifulSoup
import requests

hora=time.strftime("%I:%M")
computer="#Sheldon > "
user="#Alvaro  > "
print("")
print("")
print(computer,"Hola son las ",hora)
print(computer,"Quieres jugar (si/no)")
respuesta=str(input(user))
if(respuesta=="si"):
  print("########################################################")
  print(computer,"Prepararé la mesa de estudio para que esté despejada y tenga todo el material necesario para estudiar.")
  respuesta=str(input(user))
  print(computer,"Enlistare  los deberes que quedaron hacer??")
  respuesta=str(input(user))
  os.system("start  https://www.youtube.com/watch?v=kSkSj-OY8Uo&t=1861ss")
  os.system("start https://trello.com/b/XJuLQFXF/un20")
  print(computer,"RECUERDA qué deberes voy hacer, qué asignatura voy a estudiar y qué tengo que preparar para el día siguiente.")
  respuesta=str(input(user))
  print(computer,"RECUERDA Terminaré haciendo un repaso general y preparando la mochila para mañana.")


  respuesta=str(input(user))

#abrir un web
#os.system("start https://trello.com/b/XJuLQFXF/un20")
