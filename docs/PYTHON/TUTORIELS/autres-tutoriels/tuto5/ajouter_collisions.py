# on rajoute random
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60
vies = 3

# initialisation des tirs
tirs_liste = []

# initialisation des ennemis
ennemis_liste = []


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

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


def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])



def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)



def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])



def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le bas et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>128:
            ennemis_liste.remove(ennemi)


def vaisseau_suppression(vies):
    """disparition du vaisseau et d'un ennemi si contact"""

    for ennemi in ennemis_liste:
        if ennemi[0] <= vaisseau_x+8 and ennemi[1] <= vaisseau_y+8 and ennemi[0]+8 >= vaisseau_x and ennemi[1]+8 >= vaisseau_y:
            ennemis_liste.remove(ennemi)
            vies -=1

    return vies

def ennemis_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1] \
            and ennemi[1]<= tir[1]+4:

                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_deplacement(ennemis_liste)

    # suppression du vaisseau et ennemi si contact
    vies = vaisseau_suppression(vies)

    # suppression des ennemis et tirs si contact
    ennemis_suppression()


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # si le vaisseau possede des vies le jeu continue
    if vies > 0:

        # vaisseau (carre 8x8)
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

        # tirs
        for tir in tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)

        # ennemis
        for ennemi in ennemis_liste:
            pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)
    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)