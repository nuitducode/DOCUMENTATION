# ÉTAPE #01 - Déplacer un carré avec les touches de directions

**But** : déplacer un carré avec les touches de directions

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-01.gif" width=250 /></center>

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


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        
        # deplacement du vaisseau
        self.vaisseau_deplacement()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        
        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)

Jeu()
```

---

Auteur : Laurent Abbal - [GitHub](https://github.com/laurentabbal) | [Twitter](https://twitter.com/laurentabbal)
