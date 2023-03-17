# Premiers pas avec Pyxel - Terminale

!!! tip "Cahier Numérique pour s'entrainer"
    Ce tutoriel est disponible au format [Cahier Numérique](https://www.cahiernum.net)<br />
    :material-arrow-right-bottom: :fontawesome-solid-circle-arrow-right: [www.cahiernum.net/J682W5](https://www.cahiernum.net/J682W5)

## Étape #01 - Déplacer un carré avec les touches de directions

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

## Étape #02 - Ajouter des tirs

**But** : ajouter des tirs

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-02.gif" width=250 /></center>

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

## Étape #03 - Ajouter des ennemis

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

## Étape #04 - Ajouter les collisions

**But** : ajouter les collisions

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-04.gif" width=250 /></center>

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
        
        # vies
        self.vies = 1
        
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
                
                
    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""
        
        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies = 0                    
 
 
    def ennemis_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""
        
        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)


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
        
        # suppression des ennemis et tirs si contact
        self.ennemis_suppression()
        
        # suppression du vaisseau et ennemi si contact
        self.vaisseau_suppression()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        
        # vide la fenetre
        pyxel.cls(0)

        
        # si le vaisseau possede des vies le jeu continue
        if self.vies > 0:
            
            # vaisseau (carre 8x8)
            pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
        
            # tirs
            for tir in self.tirs_liste:
                pyxel.rect(tir[0], tir[1], 1, 4, 10)
                
            # ennemis
            for ennemi in self.ennemis_liste:
                pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)
        
        # sinon: GAME OVER
        else:
            
            pyxel.text(50,64, 'GAME OVER', 7)

Jeu()
```

## Étape #05 - Ajouter les explosions lors des collisions

**But** : ajouter les explosions lors des collisions

<center><img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-05.gif" width=250 /></center>

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
        
        # vies
        self.vies = 4
        
        # initialisation des tirs
        self.tirs_liste = []
        
        # initialisation des ennemis
        self.ennemis_liste = []
        
        # initialisation des explosions
        self.explosions_liste = []        
                
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
                
                
    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""
        
        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1
                # on ajoute l'explosion
                self.explosions_creation(self.vaisseau_x, self.vaisseau_y)
 
 
    def ennemis_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""
        
        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    self.explosions_creation(ennemi[0], ennemi[1])


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
        self.deplacement()

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
        if self.vies > 0:
            
            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(self.vies), 7)
            
            # vaisseau (carre 8x8)
            pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
        
            # tirs
            for tir in self.tirs_liste:
                pyxel.rect(tir[0], tir[1], 1, 4, 10)
                
            # ennemis
            for ennemi in self.ennemis_liste:
                pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)
                
            # explosions (cercles de plus en plus grands)
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)
            
        
        # sinon: GAME OVER
        else:
            
            pyxel.text(50,64, 'GAME OVER', 7)

Jeu()
```

## Étape #06 - Ajouter les images

**But** : ajouter les images

<center>
<img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/pyxel-tutoriel-06.gif" width="250" />
<img src="https://raw.githubusercontent.com/nuitducode/DOCUMENTATION/main/docs/assets/images/tutoriels/editeur.png" width="320" />
</center>

Pour ouvrir l'éditeur d'image : ouvrir la console (avec [Edupyter](https://www.edupyter.net/) depuis Thonny : "Outils" > "Ouvrir la console du système...", ou depuis le menu d'Edupyter : "Console") et saisir :

```
pyxel edit [PYXEL_RESOURCE_FILE]
```

"Si le fichier de ressource Pyxel (.pyxres) existe déjà, le fichier est chargé, sinon, un nouveau fichier avec le nom indiqué est créé. Si le fichier de ressource n’est pas spécifié, le nom est my_resource.pyxres." voir [documentation](https://github.com/kitao/pyxel/blob/main/docs/README.fr.md#comment-cr%C3%A9er-une-ressource)

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
        
        # vies
        self.vies = 4
        
        # initialisation des tirs
        self.tirs_liste = []
        
        # initialisation des ennemis
        self.ennemis_liste = []
        
        # initialisation des explosions
        self.explosions_liste = []
        
        # chargement des images
        pyxel.load("images.pyxres")
                
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
            self.tirs_liste.append([self.vaisseau_x, self.vaisseau_y-8])
            
            
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
                
                
    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""
        
        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1
                # on ajoute l'explosion
                self.explosions_creation(self.vaisseau_x, self.vaisseau_y)
 
 
    def ennemis_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""
        
        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi[0] <= tir[0]+8 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    self.explosions_creation(ennemi[0], ennemi[1])


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
        self.deplacement()

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
        if self.vies > 0:
            
            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(self.vies), 7)
            
            # vaisseau (carre 8x8)
            pyxel.blt(self.vaisseau_x, self.vaisseau_y, 0, 0, 0, 8, 8)
        
            # tirs
            for tir in self.tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 0, 8, 8)
                
            # ennemis
            for ennemi in self.ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0, 0, 8, 8, 8)
                
            # explosions (cercles de plus en plus grands)
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)
            
        
        # sinon: GAME OVER
        else:
            
            pyxel.text(50,64, 'GAME OVER', 7)

Jeu()
```

---

Auteur : Laurent Abbal - [GitHub](https://github.com/laurentabbal) | [Twitter](https://twitter.com/laurentabbal)


## COMPLÉMENTS

### Étape #01

Trois Parties: 

* déclaration des variables et des fonctions
* fonction update()
* fonction draw()

Exemple d'utilisation pour le déplacement du vaisseau.

#### Déclaration des variables et des fonctions 
Position du vaisseau par la création des coordonnées du vaisseau au départ. Pour l'instant il n'y a pas de vaisseau, juste deux variables `vaisseau_x` et `vaisseau_y` initialisées par les valeurs 60.

``` py
vaisseau_x = 60
vaisseau_y = 60
```

Cette fonction a pour arguments les valeurs des variables `x` et `y` et renvoie les valeurs des variables `x` et `y` modifiées suivant certaines touches du clavier.

``` py
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
```

#### Fonction update()

Cette fonction `update()` est appelé 30 fois par seconde. 

``` py
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
```

Que fait cette instruction (affectation) ?

``` py
 vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
```
 
* L'appel de la fonction `vaisseau_deplacement(vaisseau_x, vaisseau_y)` avec pour arguments les valeurs des variables `vaisseau_x` et `vaisseau_y` et renvoie les valeurs modifiées suivant certaines touches du clavier. 
* Ces valeurs renvoyées sont affectées aux variables `vaisseau_x` et `vaisseau_y`.
* Les valeurs des variables `vaisseau_x` et `vaisseau_y` sont modifiées 30 fois par seconde suivant certaines touches du clavier.

#### Fonction draw()
Enfin le dessin !
 
Pour l'instant il n'y a pas encore de vaisseau. On a créé deux variables `vaisseau_x` et `vaisseau_y` qui sont modifiées par l'appel de la fonction `update()` 30 fois par seconde permettant de réaliser cette instruction.

``` py
vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
```
 
Cette fonction draw() est appelé 30 fois par seconde.

``` py
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)
```

L'instruction `pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)` permet de dessiner un rectangle ayant comme coordonnées coin gauche les valeurs des variables `vaisseau_x` et `vaisseau_y`, de largeur 8, de hauteur 8 et de couleur 1.

A quoi sert l'instruction `python pyxel.cls(0) ` ? 

* La commenter et essayer ?
* La modifier en `python pyxel.cls(3)` et essayer ?
* La modifier en `python pyxel.cls(1)` et essayer ?

30 fois par seconde deux actions sont réalisées :

* la fenêtre graphique est remplie d'une couleur
* on dessine une rectangle

Cela donne l'illusion d'un mouvement comme au cinéma.


### Étape #02

Halo autour du tir

``` py
pyxel.rectb(tir[0]-1, tir[1]-1,3,6,3)
```

Tir sous forme cercle avec halo

``` py
pyxel.circ(tir[0], tir[1], 2, 3)
pyxel.circb(tir[0], tir[1],3,9)
```

Tir sous forme cercle avec halo clignotant

``` py
import random
pyxel.circb(tir[0], tir[1],3,random.randint(1,10))
```

### Étape #03

* Mettre en parallèle la création des tirs et des ennemis.
* Utilisation de listes pour enregistrer les coordonnées sous la forme de liste.
* Ajout de valeurs (coordonnées) par rapport au vaisseau par appui sur une touche.
* Ajout de valeurs (coordonnées) aléatoire pour l'abscisse suivant une durée.

``` py
def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])
    return tirs_liste
	
def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste
```

Mise à jour des valeurs des différentes listes suivant des conditions.

``` py
def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste
	
def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>128:
            ennemis_liste.remove(ennemi)
    return ennemis_liste
```

#### Fonction update()
La fonction `update()` est appelé 30 fois par seconde permettant la mise à jour des différentes variables.

``` py
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_liste = ennemis_deplacement(ennemis_liste) 
```

#### Fonction draw()
Enfin le dessin !
La fonction `draw()` est appelé 30 fois par seconde.

``` py
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

    # tirs
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

    # ennemis
    for ennemi in ennemis_liste:
        pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8) 
```

---

Auteur : Charles Poulmaire - [Twitter](https://twitter.com/PoulmaireC)
