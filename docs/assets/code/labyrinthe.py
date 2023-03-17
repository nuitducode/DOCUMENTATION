import pyxel, random


class Jeu:
    def __init__(self):
        """
        initialisation du jeu
        """
        pyxel.init(248,248)
        self.stage = 1
        self.mini_init()        
        pyxel.run(self.update, self.draw) 
        
    def mini_init(self):
        self.phase = "start"
        self.timer = 0
        #attributs pour la creation du labyrinthe        
        self.start = [random.choice((8, 232)), random.choice((8, 232))]
        self.goal = [240-self.start[0], 240-self.start[1]]
        self.chemin = [[8,8]]  
        self.poss = [[24, 8], [8,24]]                  
        self.pas = []        
        self.creation_lab()
        #deplacement du joueur
        self.p_x = self.start[0]
        self.p_y = self.start[1]
        self.animation = [0, None]
        self.animation_enmy1 = 0
        self.animation_enmy2 = 0  
        self.animation_enmy3 = 0 
        self.enmy3_x = 0
        self.enmy3_y = 0
        self.solution_enmy3 = []
        self.visitees = []
        #deplacement des ennemis
        self.enmy_direction = [[-8,0],[0,-8],[8,0],[0,8]]
        self.enmy_1 = [240-self.p_x, self.p_y, 0]
        self.enmy_2 = [120, 120, 0]
        self.enmy_3 = [self.p_x, 240-self.p_y]
        self.sol = 30
        self.visitees = []
        self.solution_enmy3 = []
        self.x_enmy3 = 0
        self.y_enmy3 = 0
        self.enmy_4 = [120,120]
        self.enmy4_time = 90
        self.animation_enmy4 = []
        self.torch = [[None, None], False] 

        
    def creation_lab(self):    
        """
        methode qui cree un labyrinthe de maniere aleatoire au debut du jeu
        """
        for i in range(224):            
            chemin = self.chemin
            poss = self.poss
            pas = self.pas
            #choisir la nouvelle case que l'on ajoute au chemin
            random.shuffle(poss)
            case_nv = poss[0]
            chemin.append(case_nv)
            #liste des voisins de la nouvelle case 
            prochaine_poss = [[case_nv[0],case_nv[1]-16],
                              [case_nv[0]+16,case_nv[1]],
                              [case_nv[0],case_nv[1]+16],
                              [case_nv[0]-16,case_nv[1]]]
            #ajout des voisins dans la liste possible
            for c in prochaine_poss:          
                if (c[0] in range(248)) and (c[1] in range(248)) and (c not in chemin and c not in poss):
                    poss.append(c)                    
            # choisir la passerelle
            pass_possible = [e for e in prochaine_poss if (e[0] in range(248) and e[1] in range(248) and e in self.chemin) ]            
            random.shuffle(pass_possible)
            pass_choisi = pass_possible[0]
            #relier la nouvelle case au chemin en ajoutant la passerelle
            pas.append([case_nv[0]-(case_nv[0]-pass_choisi[0])//2,case_nv[1]-(case_nv[1]-pass_choisi[1])//2])
            del poss[0]
        chemin += pas 
        
        
    def mur(self, x, y):
        """
        methode qui retourne si le joueur peut se deplacer
        """
        if [x,y] in self.chemin:
            return True
        return False 
    
    
    def update_torch(self):
        """
        methode qui gere l'utilisation de la torche
        """
        if self.animation[0] == 0 and pyxel.btn(pyxel.KEY_SPACE) and not self.torch[1]:
            self.torch = [[self.p_x, self.p_y], True]
            
        
    
    def deplacement_p(self):
        """
        methode qui gere l'animation du joueur lors de son deplacement
        """
        if self.animation[0] != 0:
            self.animation[0] += -1   
            if self.animation[1] == "right":
                self.p_x += 2
            elif self.animation[1] == "up":
                self.p_y += -2
            elif self.animation[1] == "down":
                self.p_y +=2
            else:
                self.p_x += -2
    
    def collision(self):
        """
        methode qui arrete le jeu lorsque le joueur est en collision avec un ennemi
        """
        if (self.enmy_1[:2] == [self.p_x,self.p_y]) or (self.enmy_2[:2] == [self.p_x, self.p_y]) or (self.stage >=2 and self.enmy_3 == [self.p_x, self.p_y]) or (self.stage == 3 and self.enmy_4 == [self.p_x, self.p_y]):
            self.phase = "over"
            self.timer =0
                
          
    def enmy1_update(self):
        if self.animation_enmy1 == 0:
            
            if self.enmy_1[2] == 3:
                x = 0
            else:
                x = self.enmy_1[2] + 1
            if self.enmy_1[2] == 0:
                y = 3
            else:
                y = self.enmy_1[2] - 1
            
            if self.mur(self.enmy_1[0] + self.enmy_direction[x][0] ,self.enmy_1[1] + self.enmy_direction[x][1]):
                self.enmy_1[2] = x
                self.animation_enmy1 = 4

            elif self.mur(self.enmy_1[0] + self.enmy_direction[self.enmy_1[2]][0],self.enmy_1[1] + self.enmy_direction[self.enmy_1[2]][1]):
                self.animation_enmy1 = 4
            
            elif self.mur(self.enmy_1[0] + self.enmy_direction[y][0],self.enmy_1[1] + self.enmy_direction[y][1]):
                self.enmy_1[2] = y
                self.animation_enmy1 = 4
             
            else:
                self.enmy_1[2] = x
                
    def enmy2_update(self):
        if self.animation_enmy2 == 0:
            
            liste = []
            
            if self.enmy_2[2] == 3:
                x = 0
            else:
                x = self.enmy_2[2] + 1
                
            if self.enmy_2[2] == 0:
                y = 3
            else:
                y = self.enmy_2[2] - 1
            
            if self.mur(self.enmy_2[0] + self.enmy_direction[x][0] ,self.enmy_2[1] + self.enmy_direction[x][1]):
                liste += [x]

                
            if self.mur(self.enmy_2[0] + self.enmy_direction[self.enmy_2[2]][0],self.enmy_2[1] + self.enmy_direction[self.enmy_2[2]][1]):
                liste += [self.enmy_2[2]]
            
            if self.mur(self.enmy_2[0] + self.enmy_direction[y][0],self.enmy_2[1] + self.enmy_direction[y][1]):
                liste += [y]
             
            if liste == []:                    
                self.enmy_2[2] = x
             
            else:
                self.enmy_2[2] = random.choice(liste)
                self.animation_enmy2 = 4
        
    def enmy3_update(self):
        if self.animation_enmy3 == 0:
            if self.sol > 0 and self.visitees == []:
                self.sol -= 1
            if self.sol == 0 and [self.p_x,self.p_y] in self.chemin:
                self.visitees = self.solution()
                self.visitees.pop(0)
                self.sol = 60
            if self.visitees != []:
                self.x_enmy3 = self.visitees[0][0] - self.enmy_3[0]
                self.y_enmy3 = self.visitees[0][1] - self.enmy_3[1]
                self.visitees.pop(0)
                self.animation_enmy3 = 4

    def enmy4_update(self):
        if self.enmy4_time > 0:
            self.enmy4_time -= 1
        if self.enmy4_time in range(5,10) and [self.p_x,self.p_y] in self.chemin:
            self.animation_enmy4 = [self.p_x,self.p_y]
        if self.enmy4_time == 0:
            self.enmy_4 = self.animation_enmy4
            self.enmy4_time = 90             
                
                
    def voisines (self,i,j):
        cases_voisines = []
        if [i+8,j] in self.visitees:
            cases_voisines = [i+8,j]
        if [i-8,j] in self.visitees:
            cases_voisines = [i-8,j]
        if [i,j+8] in self.visitees:
            cases_voisines = [i,j+8]
        if [i,j-8] in self.visitees:
            cases_voisines = [i,j-8]
        return cases_voisines

    def solution(self):
        chemin = [[self.enmy_3[0],self.enmy_3[1]]]
        self.visitees = []
        for n in self.chemin:
            self.visitees.append([n[0],n[1]])
        while chemin[-1] != [self.p_x,self.p_y]:
            for i in self.visitees :
                if chemin[-1][0] == i[0] and chemin[-1][1] == i[1]:
                    self.visitees.remove(i)
            if self.voisines(chemin[-1][0],chemin[-1][1]) != []:
                chemin.append(self.voisines(chemin[-1][0],chemin[-1][1]))
            else:
                chemin.pop(-1)
        return chemin
        
    def deplacement_enmy1(self):
        if self.animation_enmy1 != 0:
            self.animation_enmy1 += -1   
            self.enmy_1[0] += self.enmy_direction[self.enmy_1[2]][0]//4 
            self.enmy_1[1] += self.enmy_direction[self.enmy_1[2]][1]//4
    
    def deplacement_enmy2(self):
        if self.animation_enmy2 != 0:
            self.animation_enmy2 += -1   
            self.enmy_2[0] += self.enmy_direction[self.enmy_2[2]][0]//4 
            self.enmy_2[1] += self.enmy_direction[self.enmy_2[2]][1]//4
            
    
    def deplacement_enmy3(self):
        if self.animation_enmy3 != 0:
            self.animation_enmy3 += -1  
            self.enmy_3[0] += self.x_enmy3//4
            self.enmy_3[1] += self.y_enmy3//4
            
        
    def update_play(self):
        if self.animation[0] == 0:
            if pyxel.btn(pyxel.KEY_RIGHT) and self.mur(self.p_x+8,self.p_y):
                self.animation[0] = 4
                self.animation[1] = "right"
            if pyxel.btn(pyxel.KEY_LEFT) and self.mur(self.p_x-8,self.p_y):
                self.animation[0] = 4
                self.animation[1] = "left"
            if pyxel.btn(pyxel.KEY_DOWN) and self.mur(self.p_x,self.p_y+8):
                self.animation[0] = 4
                self.animation[1] = "down"
            if pyxel.btn(pyxel.KEY_UP) and self.mur(self.p_x,self.p_y-8):
                self.animation[0] = 4
                self.animation[1] = "up"  
            
        if [self.p_x, self.p_y] == self.goal:
            if self.stage == 3:
                self.phase = "ending"
            else:
                self.stage += 1
                self.mini_init()
               
            
        self.update_torch()

        self.collision()
        self.deplacement_p()
        self.collision()
        self.enmy1_update()
        self.deplacement_enmy1()
        self.collision()
        self.enmy2_update()
        self.deplacement_enmy2()
        self.collision()
        if self.stage >=2:
            self.enmy3_update()
            self.deplacement_enmy3()
            self.collision()
        if self.stage == 3:
            self.enmy4_update()
            self.collision()
                
            
    def update_start(self):
        self.phase = "play"   
    
    def update_ending(self):
        end.Jeu()
    
    def update(self):
        if self.phase == "start":
            self.update_start()
        elif self.phase == "play":
            self.update_play()        
        elif self.phase == "over":
            self.update_over()
        elif self.phase == "ending":
            self.update_ending()
        
    
    def draw_mur(self, c):
        """
        methode qui renvoie si le mur peut etre afficher ou non
        """
        # si le mur est dans le champ de vision du joueur
        if c[0] in range(self.p_x-16, self.p_x+17) and c[1] in range(self.p_y-16, self.p_y+17):
            return 1
        if c[0] in range(self.p_x-32, self.p_x+33) and c[1] in range(self.p_y-32, self.p_y+33):
            return 2
        if c[0] in range(self.p_x-40, self.p_x+41) and c[1] in range(self.p_y-40, self.p_y+41):
            return 3
        # si le mur est pres de la torche
        if self.torch[1] and c[0] in range(self.torch[0][0]-40, self.torch[0][0]+41) and c[1] in range(self.torch[0][1]-40, self.torch[0][1]+41):
            return 3
        return False

    def update_over(self):
        if self.timer == 90:
            self.mini_init()
        self.timer += 1 


    def draw_start(self):
        pyxel.cls(9)
        pyxel.rect(46,26,170,40,11)
        pyxel.text(60,40, 'L ODYSEE DE UTACHIN', 10)
        pyxel.text(102,180, 'PRESS ENTER', 0)
        pyxel.text(170,234, 'UTACHIN 17', 1)
        pyxel.text(102,150, 'STAGE '+str(self.stage), 8)
        
        
    def draw_play(self):
        pyxel.cls(0)
        #afficher les murs du labyrinthe
        for c in self.chemin:
            if self.draw_mur(c)==1:
                pyxel.rect(c[0], c[1], 8, 8, 7  )
            if self.draw_mur(c)==2:
                pyxel.rect(c[0], c[1], 8, 8, 10  )
            if self.draw_mur(c)==3:
                pyxel.rect(c[0], c[1], 8, 8, 9  )
            if c in self.visitees:
                pyxel.rect(c[0]+3, c[1], 2, 8, 13 )
                pyxel.rect(c[0], c[1]+3, 8, 2, 13  )
        #affiche l'ennemi 1
        pyxel.rect(self.enmy_1[0], self.enmy_1[1], 8, 8, 2)
        #affiche l'ennemi 2
        pyxel.rect(self.enmy_2[0], self.enmy_2[1], 8, 8, 4)
        #affiche l'ennemi 3
        if self.stage >= 2:
            if self.sol != 150 and self.sol not in range(0,5) and self.sol not in range(10,15) and self.sol not in range(20,25) and self.sol not in range(30,35):
                pyxel.rect(self.enmy_3[0], self.enmy_3[1], 8, 8, 5)
            else:
                pyxel.rect(self.enmy_3[0], self.enmy_3[1], 8, 8, 13)
        
        
        #affiche l'ennemi 4
        if self.stage == 3:
            pyxel.rect(self.enmy_4[0], self.enmy_4[1], 8, 8, 12)
            if self.enmy4_time in range(5,10) or self.enmy4_time in range(15,20) or self.enmy4_time in range(25,30):
                pyxel.rect(self.p_x+3, self.p_y-8, 2, 24, 12  )
                pyxel.rect(self.p_x-8, self.p_y+3, 24, 2, 12  )
                pyxel.circb(self.p_x+3, self.p_y+3, 8,  12  )
        #affiche le joueur    
        pyxel.rect(self.p_x+2, self.p_y+2, 4, 4, 8)
        #affiche l'arrivee
        pyxel.rect(self.goal[0], self.goal[1], 8, 8, 8)
        #affiche la torche
        if self.torch[1]:
            pyxel.rect(self.torch[0][0]+2, self.torch[0][1]+2, 4, 4, 9)

     
    def draw_over(self):
        pyxel.cls(0)
        pyxel.text(100,124, 'GAME OVER', 14)
    
    def draw(self):    
        if self.phase == "start":
            self.draw_start()
        elif self.phase == "play":
            self.draw_play()
        elif self.phase == "over":
            self.draw_over()
        
Jeu()
