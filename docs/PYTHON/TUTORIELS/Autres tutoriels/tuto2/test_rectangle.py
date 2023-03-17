import pyxel

# taille de la fenetre 128x128 pixels

pyxel.init(128, 128, title="test rectangles")

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
    pyxel.rect(60, 60, 50, 50, 1)

pyxel.run(update, draw)
