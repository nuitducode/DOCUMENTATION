# ÉTAPE #03 - Ajouter des ennemis

**But** : ajouter des ennemis

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-03.gif" width=250 /></center>

> Programmation orientée objet

``` py
# on rajoute random
import pyxel, random

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
        
        # initialisation des ennemis
        self.ennemis_liste = []
        
        pyxel.run(self.update, self.draw)


    def deplacement(self):
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
        """déplacement des tirs vers le haut et suppression quand ils sortent du cadre"""
        
        for tir in  self.tirs_liste:
            tir[1] -= 1
            if  tir[1]<-8:
                self.tirs_liste.remove(tir)


    def ennemis_creation(self):
        """création aléatoire des ennemis"""
        
        # un ennemi par seconde
        if (pyxel.frame_count % 30 == 0):
            self.ennemis_liste.append([random.randint(0, 120), 0])


    def ennemis_deplacement(self):
        """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""              

        for ennemi in self.ennemis_liste:
            ennemi[1] += 1
            if  ennemi[1]>128:
                self.ennemis_liste.remove(ennemi)
          

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        
        # deplacement du vaisseau
        self.deplacement()

        # creation des tirs en fonction de la position du vaisseau
        self.tirs_creation()
        
        # mise a jour des positions des tirs
        self.tirs_deplacement()
        
        # creation des ennemis
        self.ennemis_creation()
        
        # mise a jour des positions des ennemis
        self.ennemis_deplacement()            


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
            
        # ennemis
        for ennemi in self.ennemis_liste:
            pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)            

Jeu()
```

---

Auteur : Laurent Abbal - [GitHub](https://github.com/laurentabbal) | [Twitter](https://twitter.com/laurentabbal)
