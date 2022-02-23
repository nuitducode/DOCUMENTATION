# TUTORIEL #01

**But** : déplacer un carré avec les touches de directions

<center>
<iframe width="315" height="315" src="https://www.youtube.com/embed/dsml0_gn7CE" title="Tutoriel #01" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;" allowfullscreen></iframe>
</center>

## 1. Première

> Programmation impérative : utilisation obligatoire de variables globales dans `update`.

``` py
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128)

vaisseau_x = 10
vaisseau_y = 10

def deplacement(x, y):
    """ déplacement avec les touches de directions """

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 1
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 1
    return x, y


# =========================================================
# == UPDATE
# =========================================================
def update():
    """ mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    vaisseau_x, vaisseau_y = deplacement(vaisseau_x, vaisseau_y)

    # ferme la fenetre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


# =========================================================
# == DRAW
# =========================================================
def draw():
    """ création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

pyxel.run(update, draw)
```

## 2. Terminale

> Programmation orientée objet

``` py
import pyxel,random

class Jeu:
    def __init__(self):
        
        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128,128)
        
        # position initiale du vaisseau
        self.vaisseau_x = 10
        self.vaisseau_y = 10
        
        pyxel.run(self.update, self.draw)


    def deplacement(self):
        """ déplacement avec les touches de directions """
         
        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau_y<120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau_y>0:
            self.vaisseau_y += -1


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """ mise à jour des variables (30 fois par seconde)"""
        
        # deplacement du vaisseau
        self.deplacement()

        # ferme la fenetre avec la touche q
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """ création et positionnement des objets (30 fois par seconde)"""
        
        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)

Jeu()
```