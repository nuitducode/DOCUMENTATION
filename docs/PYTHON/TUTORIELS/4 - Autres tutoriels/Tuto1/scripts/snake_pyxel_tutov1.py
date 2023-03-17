import pyxel

#constantes du jeu
TITLE = "snake"
WIDTH = 200
HEIGHT = 160
CASE = 20


pyxel.init(WIDTH, HEIGHT, title=TITLE)

# les éléments du jeu
# le serpent est un tableau à 2 dimensions.
# le premier est la tête, les suivants le corps
# chaque élément est une liste de cooordonnées [abs, ord]
snake = [[3, 0], [2, 0], [1, 0]]

# le score est une variable globale
score = 0


#les 2 fonctions automatiquement appelées par Pyxel
#draw et update
def draw():
    '''
    Appelée automatiquement 30x par seconde par pyxel.
    Nettoie l'écran, dessine le serpent.
    '''
    #l'écran : effacer puis remplir de noir
    pyxel.cls(0)

       
    #le serpent
    #snake est une liste de listes de 2 coordonnées
    #exple : [[3,0], [2, 0], [1,0]] (ou plus long si le serpent est plus grand)

    # dessiner le corps en vert
    for anneau in snake[1:]:
        x, y = anneau[0], anneau[1]
        #11 est une couleur un peu verte
        pyxel.rect(x * CASE, y * CASE,
                   CASE , CASE,11)

    # dessiner la tête en orange
    x_head, y_head = snake[0]
    #9 est la couleur orange
    pyxel.rect(x_head * CASE, y_head * CASE,
               CASE , CASE ,9)

    #le score
    #7 est la couleur blanche
    pyxel.text(4, 4, f"SCORE : {score}", 7)
    
def update():
    pass

pyxel.run(update, draw)
    
