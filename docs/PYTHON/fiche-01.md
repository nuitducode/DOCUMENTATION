# FICHE #01

## 1. Première

```python
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128)

x = 10
y = 10
tirs_liste = []
ennemis_liste = []

def vaisseau(x, y):
    """ controle du vaiseau avec les touches de directions """

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
    """ """

    if pyxel.btn(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])
    return tirs_liste


def tirs_deplacemnt(x, y, tirs_liste):
    """ """

    if (tirs_liste != []):
        for tir in tirs_liste:
            tir[1] -= 1

    return tirs_liste


def ennemis_creation(ennemis_liste):
    """ """
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0,120), 0])
    return ennemis_liste


def ennemis_deplacemnt(ennemis_liste):
    """ """

    for ennemi in ennemis_liste:
        ennemi[1] += 1

    return ennemis_liste


# ==============================================================================
# == UPDATE
# ==============================================================================
def update():

    global x, y, tirs_liste, ennemis_liste

    x, y = vaisseau(x, y)
    tirs_liste = tirs_creation(x, y, tirs_liste)
    tirs_liste = tirs_deplacemnt(x, y, tirs_liste)

    ennemis_liste = ennemis_creation(ennemis_liste)
    ennemis_liste = ennemis_deplacemnt(ennemis_liste)
    print(ennemis_liste)




    # ferme la fenetre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


# ==============================================================================
# == DRAW
# ==============================================================================
def draw():

    global x, y, tirs_liste, ennemis_liste

    # vide la fenetre
    pyxel.cls(0)

    # ennemis
    for ennemi in ennemis_liste:
        pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

    # tirs vaisseau
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

    # vaisseau
    pyxel.rect(x, y, 8, 8, 1)

pyxel.run(update, draw)
```

## 2. Terminale

```python
import pyxel,random

class Jeu:
    def __init__(self):
        pyxel.init(128,128)
        self.p_x = 64
        self.p_y = 100
        self.p_alive = True
        self.blt = []
        self.enmy = []
        self.explose = []
        self.score = 0
        pyxel.load("jeu.pyxres")
        pyxel.run(self.update, self.draw)

    def shoot(self):
        new_blt = [self.p_x+3, self.p_y-4]
        self.blt.append(new_blt)

    def update_blt(self):
        for b in self.blt:
            b[1] += -3
            if  b[1]<-10:
                self.blt.remove(b)
            for e in self.enmy:
                if e[0]-1<b[0]<e[0]+9 and e[1]-4<b[1]<e[1]+12:
                    self.blt.remove(b)
                    e[2] -= 1


    def spawn(self):
        new_enmy = [random.randint(0,120), random.randint(0,10), 4]
        self.enmy.append(new_enmy)

    def update_enmy(self):
        for e in self.enmy:
            e[1] += 1
            if e[1]>120 or e[2]==0:
                self.enmy.remove(e)
                self.explosion(e[0], e[1])
                if  e[2]==0:
                    self.score += 1
            if e[0]-8<self.p_x<e[0]+8 and e[1]-8<self.p_y<e[1]+8 and self.p_alive:
                self.p_alive = False
                self.explosion(self.p_x, self.p_y)

    def explosion(self,x,y):
        new_explose = [x,y,0]
        self.explose.append(new_explose)

    def update_explosion(self):
        for ex in self.explose:
            ex[2] +=1
            if ex[2] == 12:
                self.explose.remove(ex)


    # =========================================================================
    # == UPDATE
    # =========================================================================
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.p_x<120:
            self.p_x += 4
        if pyxel.btn(pyxel.KEY_LEFT) and self.p_x>0:
            self.p_x += -4
        if pyxel.btn(pyxel.KEY_DOWN) and self.p_y<120:
            self.p_y += 4
        if pyxel.btn(pyxel.KEY_UP) and self.p_y>0:
            self.p_y += -4

        if pyxel.btnp(pyxel.KEY_SPACE, 5, 5) and self.p_alive:
            self.shoot()
        if random.random() < 0.05:
            self.spawn()

        if pyxel.btn(pyxel.KEY_ENTER) and not self.p_alive:
            self.p_alive = True
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.update_blt()
        self.update_enmy()
        self.update_explosion()


    # =========================================================================
    # == DRAW
    # =========================================================================
    def draw(self):
        pyxel.cls(0)

        for b in self.blt:
            #pyxel.rect(b[0], b[1], 1, 4, 10)
            pyxel.blt(b[0], b[1], 0, 8, 8, 8, 8)
        for e in self.enmy:
            #pyxel.rect(e[0], e[1], 8, 8, 8)
            pyxel.blt(e[0], e[1], 0, 0, 0, 8, 8)
        for ex in self.explose:
            pyxel.circb(ex[0]+4, ex[1]+4, 2*(ex[2]//4), 8+ex[2]%3)
        if self.p_alive:
            #pyxel.rect(self.p_x, self.p_y, 8, 8, 1)
            pyxel.blt(self.p_x, self.p_y, 0, 0, 8, 8, 8)
        else :
            pyxel.text(50,64, 'GAME OVER', 7)

        pyxel.text(5,5, 'SCORE '+ str(self.score), 7)

Jeu()
```