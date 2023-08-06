import pyxel

# taille de la fenetre 128x128 pixels

pyxel.init(128, 128, title="Déplacer vaisseau")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60



# =========================================================
# == UPDATE
# =========================================================
def update():
    #à faire plus tard
    pass


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre bleu 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

pyxel.run(update, draw)

