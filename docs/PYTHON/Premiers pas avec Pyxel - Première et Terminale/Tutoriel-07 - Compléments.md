# COMPLÉMENTS

## Tutoriel #01

Trois Parties: 

* déclaration des variables et des fonctions
* fonction update()
* fonction draw()

Exemple d'utilisation pour le déplacement du vaisseau.

### Déclaration des variables et des fonctions 
Position du vaisseau par la création des coordonnées du vaisseau au départ.
Pour l'instant il n'y a pas de vaisseau, juste deux variables vaisseau_x et vaisseau_y
initialisées par les valeurs 60.

``` python
vaisseau_x = 60
vaisseau_y = 60
```

Cette fonction a pour arguments les valeurs des variables x et y et renvoie les valeurs des variables x et y
modifiées suivant certaines touches du clavier.
``` python
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

### Fonction update()

Cette fonction update() est appelé 30 fois par seconde. 
``` python
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
```

Que fait cette instruction (affectation) ?

``` python   
 vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
 ```
 
L'appel de la fonction vaisseau_deplacement(vaisseau_x, vaisseau_y) avec pour arguments les valeurs des variables 
vaisseau_x et vaisseau_y et renvoie les valeurs modifiées suivant certaines touches du clavier. 
Ces valeurs renvoyées sont affectées aux variables vaisseau_x et vaisseau_y.
Les valeurs des variables vaisseau_x et vaisseau_y sont modifiées 30 fois par seconde suivant certaines touches du clavier.

### Fonction draw()
Enfin le dessin !
 
Pour l'instant il n'y a pas encore de vaisseau. On a créé deux variables vaisseau_x et vaisseau_y qui sont
modifiées par l'appel de la fonction update() 30 fois par seconde permettant de réaliser cette instruction 
``` python   
 vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
 ```
 
Cette fonction draw() est appelé 30 fois par seconde.

``` python 
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)
 ```

Cette instruction ``` python pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)``` permet 
de dessiner un rectangle ayant comme coordonnées coin gauche les valeurs des variables vaisseau_x et vaisseau_y,
de largeur 8, de hauteur 8 et de couleur 1.

A quoi sert cette instruction ? 
``` python pyxel.cls(0) ```

La commenter et essayer ?
La modifier en ``` python pyxel.cls(3) ``` et essayer ?
La modifier en ``` python pyxel.cls(1) ``` et essayer ?

30 fois par seconde deux actions sont réalisées :
- la fenêtre graphique est remplie d'une couleur
- on dessine une rectangle

Cela donne l'illusion d'un mouvement comme au cinéma.


## Tutoriel #02

Halo autour du tir
``` python

pyxel.rectb(tir[0]-1, tir[1]-1,3,6,3)

```

tir sous forme cercle avec halo

``` python

pyxel.circ(tir[0], tir[1], 2, 3)
pyxel.circb(tir[0], tir[1],3,9)

```

tir sous forme cercle avec halo clignotant
``` python

import random
pyxel.circb(tir[0], tir[1],3,random.randint(1,10))

```

## Tutoriel #03

Mettre en parallèle la création des tirs et des ennemis.
Utilisation de listes pour enregistrer les coordonnées sous la forme de liste.
Ajout de valeurs (coordonnées) par rapport au vaisseau par appui sur une touche.
Ajout de valeurs (coordonnées) aléatoire pour l'abscisse suivant une durée.

``` python

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

``` python
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

### Fonction update()
La fonction update() est appelé 30 fois par seconde permettant la mise à jour des différentes variables.

``` python
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

### Fonction draw()
Enfin le dessin !
La fonction draw() est appelé 30 fois par seconde.
``` python
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
