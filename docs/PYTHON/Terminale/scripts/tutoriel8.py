# -*- coding: utf-8 -*-
# on rajoute random
import pyxel, random

class Vaisseau :
    def __init__(self, x, y):
        # position initiale du vaisseau
        # (origine des positions : coin haut gauche)
        self.x = x
        self.y = y
        
        # vies
        self.vies = 4

    def draw(self) :
        # vaisseau (carre 8x8)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)
        
    def deplacement(self) :
        
        """déplacement avec les touches de directions"""
        if pyxel.btn(pyxel.KEY_RIGHT) and (self.x < 120) :
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
            self.x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y<120:
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.y>0:
            self.y += -1
        
class Tir :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8)     
        
class Monstre :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def draw(self):
       
        #Change l'aspect tous les 1/10 de secondes
        #coef peut vaaloir 0,1 ou 2
        coef = pyxel.frame_count //3% 3
        pyxel.blt(self.x, self.y, 0, 0, 8 + 8*coef, 8, 8) 
        
        
class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="Nuit du c0de")


        self.vaisseau = Vaisseau(60, 60)



        # initialisation des tirs
        self.tirs_liste = []

        # initialisation des ennemis
        self.ennemis_liste = []

        # initialisation des explosions
        self.explosions_liste = []

        # chargement des images
        pyxel.load("images.pyxres")

        pyxel.run(self.update, self.draw)





    def tirs_creation(self):
        """création d'un tir avec la barre d'espace"""

        if pyxel.btnr(pyxel.KEY_SPACE):
            self.tirs_liste.append(Tir(self.vaisseau.x, self.vaisseau.y-8))


    def tirs_deplacement(self):
        """déplacement des tirs vers le haut et suppression quand ils sortent du cadre"""

        for tir in  self.tirs_liste:
            tir.y -= 1
            if  tir.y < -8:
                self.tirs_liste.remove(tir)


    def ennemis_creation(self):
        """création aléatoire des ennemis"""

        # un ennemi par seconde
        if (pyxel.frame_count % 30 == 0):
            self.ennemis_liste.append(Monstre(random.randint(0, 120), 0))


    def ennemis_deplacement(self):
        """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""              

        for ennemi in self.ennemis_liste:
            ennemi.y += 1
            if  ennemi.y>128:
                self.ennemis_liste.remove(ennemi)


    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""

        for ennemi in self.ennemis_liste:
            if ennemi.x <= self.vaisseau.x+8 and ennemi.y <= self.vaisseau.y+8 and ennemi.x+8 >= self.vaisseau.x and ennemi.y+8 >= self.vaisseau.y:
                self.ennemis_liste.remove(ennemi)
                self.vaisseau.vies -= 1
                # on ajoute l'explosion
                self.explosions_creation(self.vaisseau.x, self.vaisseau.y)


    def ennemis_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""

        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi.x <= tir.x+8 and ennemi.x+8 >= tir.x and ennemi.y+8 >= tir.y:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    self.explosions_creation(ennemi.x, ennemi.y)


    def explosions_creation(self, x, y):
        """explosions aux points de collision entre deux objets"""
        self.explosions_liste.append([x, y, 0])


    def explosions_animation(self):
        """animation des explosions"""
        for explosion in self.explosions_liste:
            explosion[2] +=1
            if explosion[2] == 12:
                self.explosions_liste.remove(explosion)


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.vaisseau.deplacement()

        # creation des tirs en fonction de la position du vaisseau
        self.tirs_creation()

        # mise a jour des positions des tirs
        self.tirs_deplacement()

        # creation des ennemis
        self.ennemis_creation()

        # mise a jour des positions des ennemis
        self.ennemis_deplacement()

        # suppression des ennemis et tirs si contact
        self.ennemis_suppression()

        # suppression du vaisseau et ennemi si contact
        self.vaisseau_suppression()

        # evolution de l'animation des explosions
        self.explosions_animation()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)


        # si le vaisseau possede des vies le jeu continue
        if self.vaisseau.vies > 0:

            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(self.vaisseau.vies), 7)

            self.vaisseau.draw()
            
            
            # tirs
            for tir in self.tirs_liste:
                tir.draw()

            # ennemis
            for ennemi in self.ennemis_liste:
                ennemi.draw()
                

            # explosions (cercles de plus en plus grands)
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)


        # sinon: GAME OVER
        else:

            pyxel.text(50,64, 'GAME OVER', 7)

Jeu()

