import requests
import os

#============
code = 'sk6g'
#============

jeu = 'jeu_'+code+'.pyxapp'
data = requests.get('https://www.nuitducode.net/python_jeux/'+jeu)
with open(jeu, 'wb') as file:
    file.write(data.content)
os.system('pyxel play '+ jeu)
