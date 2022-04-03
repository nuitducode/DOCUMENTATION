# TUTORIEL #02 - Ajouter des tirs

**But** : ajouter des tirs

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/PYTHON/Premiers%20pas%20avec%20Pyxel%20-%20Premi%C3%A8re%20et%20Terminale/images/pyxel-tutoriel-02.gif" width=250 /></center>

## 1. Première

> Programmation impérative : utilisation obligatoire de variables globales dans `update`.

``` py
import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60

# initialisation des tirs
tirs_liste = []


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
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)
    
    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

    # tirs
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

pyxel.run(update, draw)
```

## 2. Terminale

> Programmation orientée objet

``` py
import pyxel

class Jeu:
    def __init__(self):
        
        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="Nuit du c0de")
        
        # position initiale du vaisseau
        # (origine des positions : coin haut gauche)
        self.vaisseau_x = 60
        self.vaisseau_y = 60
        
        # initialisation des tirs
        self.tirs_liste = []
        
        pyxel.run(self.update, self.draw)


    def vaisseau_deplacement(self):
        """déplacement avec les touches de directions"""
         
        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau_y<120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau_y>0:
            self.vaisseau_y += -1
           
           
    def tirs_creation(self):
        """création d'un tir avec la barre d'espace"""
        
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.tirs_liste.append([self.vaisseau_x+4, self.vaisseau_y-4])
            
            
    def tirs_deplacement(self):
        """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""
        
        for tir in  self.tirs_liste:
            tir[1] -= 1
            if  tir[1]<-8:
                self.tirs_liste.remove(tir)


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        
        # deplacement du vaisseau
        self.vaisseau_deplacement()

        # creation des tirs en fonction de la position du vaisseau
        self.tirs_creation()
        
        # mise a jour des positions des tirs
        self.tirs_deplacement()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        
        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
        
        # tirs
        for tir in self.tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)        

Jeu()
```

---

Auteur : Laurent Abbal - [GitHub](https://github.com/laurentabbal) | [Twitter](https://twitter.com/laurentabbal)
