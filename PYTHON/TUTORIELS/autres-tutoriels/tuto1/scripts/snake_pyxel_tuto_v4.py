import pyxel
from random import randint
#constantes du jeu
TITLE = "snake"
WIDTH = 200
HEIGHT = 160
CASE = 20
FRAME_REFRESH = 15

pyxel.init(WIDTH, HEIGHT, title=TITLE)

# les éléments du jeu
# le serpent est un tableau à 2 dimensions.
# le premier est la tête, les suivants le corps
# chaque élément est une liste de cooordonnées [abs, ord]

snake = [[3, 0], [2, 0], [1, 0]]
direction = [1,0]
score = 0
food = [8,3]


#les 2 fonctions automatiquement appelées par Pyxel
#draw et update
def draw():
    '''
    Appelée automatiquement 30x par seconde par pyxel.
    Nettoie l'écran, dessine le serpent.
    '''
    #l'écran : effacer puis remplir de noir
    pyxel.cls(0)
    
    #la nourriture :
    #food est une variable globale,  liste de 2 entiers (coords de la case où il y a la pomme)
    x_food, y_food = food
    #8 est la couleur rose
    pyxel.rect(x_food * CASE, y_food * CASE,CASE, CASE,8)
       
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
    global direction, food, score
    #on écoute les interactions du joueur (30 x par seconde)
    if pyxel.btn(pyxel.KEY_ESCAPE):
        exit()
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in ([0, 1], [0, -1]):
        direction = [1, 0]
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in ([0, 1], [0, -1]):
        direction = [-1, 0]
    elif pyxel.btn(pyxel.KEY_UP) and direction in ([1, 0], [-1, 0]):
        direction = [0, -1]
    elif pyxel.btn(pyxel.KEY_DOWN) and direction in ([1, 0], [-1, 0]):
        direction = [0, 1]
    if pyxel.frame_count % FRAME_REFRESH==0:
        # la nouvelle tête est l'ancienne, déplacée dans la direction
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        # on l'insère au début
        snake.insert(0, head)
        
        # mort du serpent ?
        # s'il touche son corps ou s'il quitte l'écran
        if head in snake[1:] \
                or head[0] < 0 \
                or head[0] > WIDTH/CASE - 1 \
                or head[1] < 0 \
                or head[1] > HEIGHT/CASE - 1:
            exit()
        
         #collision tête / pomme
        if snake[0]==food:
            #on augmente le score
            print("eaten !")
            score += 1
            print("score", score)
            #on replace une nouvelle pomme en-dehors du corps du serpent
            while food in snake:
                # nécessaire de tirer plusieurs fois si on n'a pas de chance !
                food = [randint(0, WIDTH/CASE - 1),
                         randint(0, HEIGHT/CASE - 1)]
            #sortie du while : on a trouvé une nouvelle case pour la pomme
            print("new food ", food)
        else:
        #si le serpent n'a pas mangé, on supprime le dernier anneau pour qu'il garde une taille constante
            snake.pop(-1)
pyxel.run(update, draw)
    





