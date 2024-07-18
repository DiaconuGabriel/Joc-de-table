import pygame
import random
import sys
import os
import time
import socket
import pickle

LATIME=1050
LUNGIME=700
MARIME_ZAR=35
MARIME_PIESA=75
GREEN=(0,255,0)
RED=(255,0,0)
BLACK=(0,0,0)
FPS=100
SERVER = socket.gethostbyname(socket.gethostname())

pygame.init()

class Zar:

    def __init__(self,zar):
        self.imagine_zar=pygame.transform.scale(zar,(MARIME_ZAR,MARIME_ZAR))
        
    def draw(self,coord_x,coord_y):
        self.coord_x=coord_x
        self.coord_y=coord_y
        fereastra.blit(self.imagine_zar,(self.coord_x,self.coord_y))

class Piesa:
    
    coordonate_de_baza_zone={0:[479,610],
                        1:[905,605],
                        2:[833,605],
                        3:[761,605],
                        4:[690,605],
                        5:[621,605],
                        6:[550,605],
                        7:[410,605],
                        8:[342,605],
                        9:[271,605],
                        10:[202,605],
                        11:[132,605],
                        12:[65,605],
                        13:[65,15],
                        14:[132,15],
                        15:[202,15],
                        16:[271,15],
                        17:[342,15],
                        18:[410,15],
                        19:[550,15],
                        20:[621,15],
                        21:[690,15],
                        22:[760,15],
                        23:[833,15],
                        24:[905,15],
                        25:[479,15],
                        -1:[1100,0],
                        26:[1200,0]}
    
    def __init__(self,zona,id,x,y,nr_buton):
        self.id=id
        if self.id=='maro':
            self.imagine=piesa_maro
        elif self.id=='negru':
            self.imagine=piesa_neagra
        self.zona=zona
        self.rect=self.imagine.get_rect()
        self.rect.topleft=(x,y)
        self.nr_buton=nr_buton
        self.apasat=False
        self.x=x
        self.y=y

    def draw1(self):
        fereastra.blit(self.imagine,(self.x,self.y))
        
    def draw(self):
        fereastra.blit(self.imagine,(self.x,self.y))
        self.verifica()
        
    def verifica(self):

        if tura_player==True and len(lista_n_player)>2 and lista_n_player[-2]<=6 :
            if f==0:
                if len(muta_piesa_neagra_disponibila(lista_n_player[-2]))==0:
                    if len(muta_piesa_neagra_disponibila(lista_m_player[-2]))==0:
                        lista_n_player[-1]=0
                        lista_m_player[-1]=0
                    if len(muta_piesa_neagra_disponibila(lista_m_player[-2]))>0:
                        if lista_m_player[-1]!=0:
                            pass
                        else:
                            lista_n_player[-1]=0       
                elif len(muta_piesa_neagra_disponibila(lista_n_player[-2]))>0:
                    if len(muta_piesa_neagra_disponibila(lista_m_player[-2]))==0:
                        if lista_n_player[-1]==0:
                            lista_m_player[-1]=0
                    elif len(muta_piesa_neagra_disponibila(lista_m_player[-2]))>0:
                        pass
            positie=pygame.mouse.get_pos()
            if self.rect.collidepoint(positie) and self.id=='negru':
                if zar_m_selectat==True and zar_n_selectat==False and lista_m_player[-1]==0:
                    if pygame.mouse.get_pressed()[0]:
                        fereastra.blit(text7,(510,750))
                if zar_n_selectat==True and zar_m_selectat==False and lista_n_player[-1]==0:
                    if pygame.mouse.get_pressed()[0]:
                        fereastra.blit(text7,(510,750))
                if zar_n_selectat==True and zar_m_selectat==False and lista_n_player[-1]>0:
                    if pygame.mouse.get_pressed()[0] and len(zone[25])<=0:
                        if zone[self.zona][-1].zona-val_zar_n < 1:
                            if self.nr_buton==zone[self.zona][-1].nr_buton:
                                if verifica_piese_negre()==True:
                                    if zone[self.zona][-1].zona==val_zar_n:
                                        zone[-2].append(zone[self.zona][-1])
                                        zone[self.zona].remove(zone[self.zona][-1])
                                        zone[-2][-1].zona=-1
                                        self.schimba_poz()
                                        lista_n_player[-1]-=1
                                    elif zone[self.zona][-1].zona!=val_zar_n:
                                        if verifica_piese_inainte_a_scoate_negre(zone[self.zona][-1].zona)==0:
                                            zone[-2].append(zone[self.zona][-1])
                                            zone[self.zona].remove(zone[self.zona][-1])
                                            zone[-2][-1].zona=-1
                                            self.schimba_poz()
                                            lista_n_player[-1]-=1
                                        elif verifica_piese_inainte_a_scoate_negre(zone[self.zona][-1].zona)>0:
                                            fereastra.blit(text14,(620,750))
                                elif verifica_piese_negre()==False:
                                    fereastra.blit(text4,(580,750))
                            elif self.nr_buton!=zone[self.zona][-1].nr_buton:
                                fereastra.blit(text5,(520,750))
                        elif zone[self.zona][-1].zona-val_zar_n >=1:
                            if self.nr_buton==zone[self.zona][-1].nr_buton: 
                                if len(zone[self.zona-val_zar_n])==0:
                                    self.zona-=val_zar_n
                                    lista_n_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_n()
                                    pygame.mouse.get_pressed()[0]==False
                                elif len(zone[self.zona-val_zar_n])==1:
                                    if zone[self.zona-val_zar_n][-1].id=='maro':
                                        zone[self.zona-val_zar_n][-1].zona=0
                                        zone[self.zona-val_zar_n][-1].schimba_poz()
                                        zone[0].append(zone[self.zona-val_zar_n][-1])
                                        zone[self.zona-val_zar_n].remove(zone[self.zona-val_zar_n][-1])
                                        self.zona-=val_zar_n
                                        lista_n_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_n()
                                        pygame.mouse.get_pressed()[0]==False
                                    elif zone[self.zona-val_zar_n][-1].id=='negru':
                                        self.zona-=val_zar_n
                                        lista_n_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_n()
                                        pygame.mouse.get_pressed()[0]==False
                                elif len(zone[self.zona-val_zar_n])>=2:
                                    if zone[self.zona-val_zar_n][-1].id=='maro':
                                        fereastra.blit(text3,(620,750))
                                    else:
                                        self.zona-=val_zar_n
                                        lista_n_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_n()
                                        pygame.mouse.get_pressed()[0]==False
                            elif self.nr_buton!=zone[self.zona][-1].nr_buton:
                                fereastra.blit(text5,(520,750))
                    elif pygame.mouse.get_pressed()[0] and len(zone[25])>0:
                        if self.nr_buton!=zone[25][-1].nr_buton:
                            fereastra.blit(text6,(670,750))
                        elif self.nr_buton==zone[25][-1].nr_buton:
                            if len(zone[self.zona-val_zar_n])==0:
                                self.zona-=val_zar_n
                                lista_n_player[-1]-=1
                                self.schimba_poz()
                                self.modifica_zona_n()
                                pygame.mouse.get_pressed()[0]==False
                            elif len(zone[self.zona-val_zar_n])==1:
                                if zone[self.zona-val_zar_n][-1].id=='maro':
                                    zone[self.zona-val_zar_n][-1].zona=0
                                    zone[self.zona-val_zar_n][-1].schimba_poz()
                                    zone[0].append(zone[self.zona-val_zar_n][-1])
                                    zone[self.zona-val_zar_n].remove(zone[self.zona-val_zar_n][-1])
                                    self.zona-=val_zar_n
                                    lista_n_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_n()
                                    pygame.mouse.get_pressed()[0]==False
                                elif zone[self.zona-val_zar_n][-1].id=='negru':
                                    self.zona-=val_zar_n
                                    lista_n_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_n()
                                    pygame.mouse.get_pressed()[0]==False
                            elif len(zone[self.zona-val_zar_n])>=2:
                                if zone[self.zona-val_zar_n][-1].id=='maro':
                                    fereastra.blit(text3,(620,750))
                                else:
                                    self.zona-=val_zar_n
                                    lista_n_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_n()
                                    pygame.mouse.get_pressed()[0]==False
                if zar_m_selectat==True and zar_n_selectat==False and lista_m_player[-1]>0:
                    if pygame.mouse.get_pressed()[0] and len(zone[25])<=0:
                        if zone[self.zona][-1].zona-val_zar_m<1:
                            if self.nr_buton==zone[self.zona][-1].nr_buton:
                                if verifica_piese_negre()==True:
                                    if zone[self.zona][-1].zona==val_zar_m:
                                        zone[-2].append(zone[self.zona][-1])
                                        zone[self.zona].remove(zone[self.zona][-1])
                                        zone[-2][-1].zona=-1
                                        self.schimba_poz()
                                        lista_m_player[-1]-=1
                                    elif zone[self.zona][-1].zona!=val_zar_m:
                                        if verifica_piese_inainte_a_scoate_negre(zone[self.zona][-1].zona)==0:
                                            zone[-2].append(zone[self.zona][-1])
                                            zone[self.zona].remove(zone[self.zona][-1])
                                            zone[-2][-1].zona=-1
                                            self.schimba_poz()
                                            lista_m_player[-1]-=1
                                        elif verifica_piese_inainte_a_scoate_negre(zone[self.zona][-1].zona)>0:
                                            fereastra.blit(text14,(620,750))
                                elif verifica_piese_negre()==False :
                                    fereastra.blit(text4,(580,750))
                            elif self.nr_buton!=zone[self.zona][-1].nr_buton:
                                fereastra.blit(text5,(520,750))
                        elif zone[self.zona][-1].zona-val_zar_m >=1:
                            if self.nr_buton==zone[self.zona][-1].nr_buton: 
                                if len(zone[self.zona-val_zar_m])==0:
                                    self.zona-=val_zar_m
                                    lista_m_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_m()
                                    pygame.mouse.get_pressed()[0]==False
                                elif len(zone[self.zona-val_zar_m])==1:
                                    if zone[self.zona-val_zar_m][-1].id=='maro':
                                        zone[self.zona-val_zar_m][-1].zona=0
                                        zone[self.zona-val_zar_m][-1].schimba_poz()
                                        zone[0].append(zone[self.zona-val_zar_m][-1])
                                        zone[self.zona-val_zar_m].remove(zone[self.zona-val_zar_m][-1])
                                        self.zona-=val_zar_m
                                        lista_m_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_m()
                                        pygame.mouse.get_pressed()[0]==False
                                    elif zone[self.zona-val_zar_m][-1].id=='negru':
                                        self.zona-=val_zar_m
                                        lista_m_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_m()
                                        pygame.mouse.get_pressed()[0]==False
                                elif len(zone[self.zona-val_zar_m])>=2:
                                    if zone[self.zona-val_zar_m][-1].id=='maro':
                                        fereastra.blit(text3,(620,750))
                                    else:
                                        self.zona-=val_zar_m
                                        lista_m_player[-1]-=1
                                        self.schimba_poz()
                                        self.modifica_zona_m()
                                        pygame.mouse.get_pressed()[0]==False
                            elif self.nr_buton!=zone[self.zona][-1].nr_buton:
                                fereastra.blit(text5,(520,750))
                    elif pygame.mouse.get_pressed()[0] and len(zone[25])>0:
                        if self.nr_buton!=zone[25][-1].nr_buton:
                            fereastra.blit(text6,(670,750))
                        elif self.nr_buton==zone[25][-1].nr_buton:
                            if len(zone[self.zona-val_zar_m])==0:
                                self.zona-=val_zar_m
                                lista_m_player[-1]-=1
                                self.schimba_poz()
                                self.modifica_zona_m()
                                pygame.mouse.get_pressed()[0]==False
                            elif len(zone[self.zona-val_zar_m])==1:
                                if zone[self.zona-val_zar_m][-1].id=='maro':
                                    zone[self.zona-val_zar_m][-1].zona=0
                                    zone[self.zona-val_zar_m][-1].schimba_poz()
                                    zone[0].append(zone[self.zona-val_zar_m][-1])
                                    zone[self.zona-val_zar_m].remove(zone[self.zona-val_zar_m][-1])
                                    self.zona-=val_zar_m
                                    lista_m_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_m()
                                    pygame.mouse.get_pressed()[0]==False
                                elif zone[self.zona-val_zar_m][-1].id=='negru':
                                    self.zona-=val_zar_m
                                    lista_m_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_m()
                                    pygame.mouse.get_pressed()[0]==False
                            elif len(zone[self.zona-val_zar_m])>=2:
                                if zone[self.zona-val_zar_m][-1].id=='maro':
                                    fereastra.blit(text3,(620,750))
                                else:
                                    self.zona-=val_zar_m
                                    lista_m_player[-1]-=1
                                    self.schimba_poz()
                                    self.modifica_zona_m()
                                    pygame.mouse.get_pressed()[0]==False

        self.rect.topleft=(self.x,self.y)    
    def schimba_poz(self):
        x_fin=Piesa.coordonate_de_baza_zone[self.zona][0]
        y_fin=Piesa.coordonate_de_baza_zone[self.zona][1]
        self.x=x_fin
        if self.zona<13:
            if len(zone[self.zona])>=5:
                self.rect.y=y_fin-(((len(zone[self.zona]))-5)*60)
                self.y=self.rect.y
            else:
                self.rect.y=y_fin-((len(zone[self.zona]))*60)
                self.y=self.rect.y
        if self.zona==13:
            if len(zone[self.zona])>=5:
                self.rect.y=y_fin+(((len(zone[self.zona]))-5)*60)
                self.y=self.rect.y
            else:
                self.rect.y=y_fin+((len(zone[self.zona]))*60)
                self.y=self.rect.y
        if self.zona>13:
            if len(zone[self.zona])>=5:
                self.rect.y=y_fin+(((len(zone[self.zona]))-5)*60)
                self.y=self.rect.y
            else:
                self.rect.y=y_fin+((len(zone[self.zona]))*60)
                self.y=self.rect.y
        
    def modifica_zona_n(self):
        if self.id=='negru':
            zone[self.zona].append(zone[self.zona+val_zar_n][-1])
            zone[self.zona+val_zar_n].remove(zone[self.zona+val_zar_n][-1])

    def modifica_zona_m(self):
        if self.id=='negru':
            zone[self.zona].append(zone[self.zona+val_zar_m][-1])
            zone[self.zona+val_zar_m].remove(zone[self.zona+val_zar_m][-1])

font = pygame.font.Font('freesansbold.ttf', 32)
font1= pygame.font.Font('freesansbold.ttf', 42)
        
fereastra = pygame.display.set_mode((LATIME,825))
imagine_fundal=pygame.image.load(os.path.join('imagini','board.jpg'))
imagine_fundal_final=pygame.transform.scale(imagine_fundal,(LATIME,LUNGIME))
fundal_inceput=pygame.image.load(os.path.join('imagini','start.jpg'))
fundal_inceput_final=pygame.transform.scale(fundal_inceput,(LATIME,825))
buton_de_start=pygame.image.load(os.path.join('imagini','buton_start.png'))
buton_de_start_final=pygame.transform.scale(buton_de_start,(200,100))
buton_de_stop=pygame.image.load(os.path.join('imagini','buton_stop.png'))
buton_de_stop_final=pygame.transform.scale(buton_de_stop,(200,100))
piesa1=pygame.image.load(os.path.join('imagini','piesa_maro.png'))
piesa_maro=pygame.transform.scale(piesa1,(MARIME_PIESA,MARIME_PIESA))
piesa2=pygame.image.load(os.path.join('imagini','piesa_neagra.png'))
piesa_neagra=pygame.transform.scale(piesa2,(MARIME_PIESA,MARIME_PIESA))
piesa_neagra_scoasa=pygame.image.load(os.path.join('imagini','piesa_neagra_de_sus.png'))
piesa_neagra_scoasa1=pygame.transform.scale(piesa_neagra_scoasa,(52,14))
piesa_maro_scoasa=pygame.image.load(os.path.join('imagini','piesa_maro_de_sus.png'))
piesa_maro_scoasa1=pygame.transform.scale(piesa_maro_scoasa,(50,14))

imagine_de_ales=pygame.image.load(os.path.join('imagini','buton_cu_calculatorul.png'))
imagine_de_ales_final=pygame.transform.scale(imagine_de_ales,(500,400))

imagine_de_ales1=pygame.image.load(os.path.join('imagini','buton_cu_player.png'))
imagine_de_ales_final1=pygame.transform.scale(imagine_de_ales1,(520,400))

menu=pygame.image.load(os.path.join('imagini','menu.png'))
buton_menu=pygame.transform.scale(menu,(400,350))

text_calculator = font.render('Calculator', True, GREEN)
text_player = font.render('Player', True, GREEN)
text_player1 = font.render('Player1', True, GREEN)
text_calculator_la_mutare=font.render('Calculatorul la mutare', True, GREEN)
text_player1_la_mutare=font.render('Player1 la mutare', True, GREEN)
text3 = font.render('Nu poti muta acolo', True, GREEN)
text4 = font.render('Nu poti scoate piesa inca', True, GREEN)
text5 = font.render('Apasa pe ultima piesa ca sa muti', True, GREEN)
text6 = font.render('Ai piesa afara', True, GREEN)
text7 = font.render('Ai consumat mutarile cu acel zar', True, GREEN)
text8 = font.render('Da cu zarul!', True, GREEN)
text9 = font.render('Se asteapta jucator.......', True, GREEN)
text10 = font.render('Ai pierdut!', True, GREEN)
text11 = font.render('Ai castigat!', True, GREEN)
text12 = font1.render('Nu te-ai putut conecta!', True, GREEN)
text13 = font1.render('Celalalt player s-a deconectat!', True, GREEN)
text14 = font.render('Mai ai piese de scos!', True, GREEN)

pygame.display.set_caption('Table')

zar1_final_1=Zar(zar=pygame.image.load(os.path.join('imagini','zar1.jpg')))
zar2_final_2=Zar(zar=pygame.image.load(os.path.join('imagini','zar2.jpg')))
zar3_final_3=Zar(zar=pygame.image.load(os.path.join('imagini','zar3.jpg')))
zar4_final_4=Zar(zar=pygame.image.load(os.path.join('imagini','zar4.jpg')))
zar5_final_5=Zar(zar=pygame.image.load(os.path.join('imagini','zar5.jpg')))
zar6_final_6=Zar(zar=pygame.image.load(os.path.join('imagini','zar6.jpg')))

zaruri=[zar1_final_1,zar2_final_2,zar3_final_3,zar4_final_4,zar5_final_5,zar6_final_6]

#in zona 6 la inceput sunt:
buton1=Piesa(6,'negru',550,605,1)
buton2=Piesa(6,'negru',550,545,2)
buton3=Piesa(6,'negru',550,485,3)
buton4=Piesa(6,'negru',550,425,4)
buton5=Piesa(6,'negru',550,365,5)

#in zona 19 la inceput sunt:
buton16=Piesa(19,'maro',550,15,16)
buton17=Piesa(19,'maro',550,75,17)
buton18=Piesa(19,'maro',550,135,18)
buton19=Piesa(19,'maro',550,195,19)
buton20=Piesa(19,'maro',550,255,20)

#in zona 24 la inceput sunt:
buton6=Piesa(24,'negru',905,15,6)
buton7=Piesa(24,'negru',905,75,7)

#in zona 1 la inceput sunt:
buton21=Piesa(1,'maro',905,605,21)
buton22=Piesa(1,'maro',905,545,22)

#in zona 17 la inceput sunt:
buton23=Piesa(17,'maro',342,15,23)
buton24=Piesa(17,'maro',342,75,24)
buton25=Piesa(17,'maro',342,135,25)

#in zona 8 la inceput sunt:
buton8=Piesa(8,'negru',342,605,8)
buton9=Piesa(8,'negru',342,545,9)
buton10=Piesa(8,'negru',342,485,10)

#in zona 12 la inceput sunt
buton26=Piesa(12,'maro',65,605,26)
buton27=Piesa(12,'maro',65,545,27)
buton28=Piesa(12,'maro',65,485,28)
buton29=Piesa(12,'maro',65,425,29)
buton30=Piesa(12,'maro',65,365,30)

#in zona 13 la inceput sunt:
buton11=Piesa(13,'negru',65,15,11)
buton12=Piesa(13,'negru',65,75,12)
buton13=Piesa(13,'negru',65,135,13)
buton14=Piesa(13,'negru',65,195,14)
buton15=Piesa(13,'negru',65,255,15)

butoane=[buton1,buton2,buton3,buton4,buton5,buton6,buton7,buton8,buton9,buton10,buton11,buton12,buton13,buton14,buton15,buton16,buton17,buton18,buton19,buton20,buton21,buton22,buton23,buton24,buton25,buton26,buton27,buton28,buton29,buton30]

zona0=[]
zona1=[buton21,buton22]
zona2=[]
zona3=[]
zona4=[]
zona5=[]
zona6=[buton1,buton2,buton3,buton4,buton5]
zona7=[]
zona8=[buton8,buton9,buton10]
zona9=[]
zona10=[]
zona11=[]
zona12=[buton26,buton27,buton28,buton29,buton30]
zona13=[buton11,buton12,buton13,buton14,buton15]
zona14=[]
zona15=[]
zona16=[]
zona17=[buton23,buton24,buton25]
zona18=[]
zona19=[buton16,buton17,buton18,buton19,buton20]
zona20=[]
zona21=[]
zona22=[]
zona23=[]
zona24=[buton6,buton7]
zona25=[]
zona_1=[]
zona26=[]

zone=[zona0,zona1,zona2,zona3,zona4,zona5,zona6,zona7,zona8,zona9,zona10,zona11,zona12,zona13,zona14,zona15,zona16,zona17,zona18,zona19,zona20,zona21,zona22,zona23,zona24,zona25,zona_1,zona26]

f=1
lista_n_player=[88,88]
lista_m_player=[88,88]
lista_n_calculator=[88,88]
lista_m_calculator=[88,88]
tura_player=True
tura_player1=False
tura_calculator=False
zar_n_selectat=False 
zar_m_selectat=False
nr_random_pt_calculator=0
val_zar_n=0 
val_zar_m=0
val_zar_n_calculator=0
val_zar_m_calculator=0


def deseneaza_butoane():
    for i in range(len(butoane)):
        butoane[i].draw()

def deseneaza_butoane1():
    for i in range(len(butoane)):
        butoane[i].draw1()

def verifica_piese_negre():
    lista_piese_pe_tabla_negre=[]
    for i in range(7,25):
        if len(zone[i])>=1:
            if zone[i][-1].id=='negru':
                lista_piese_pe_tabla_negre.append(i)
    if len(lista_piese_pe_tabla_negre)==0:
        return True
    else:
        return False

def cauta_disponibilitate_piese_negre():
    lista=[]
    if len(zone[25])==0:
        for i in range(0,25):
            if len(zone[i])!=0:
                if zone[i][-1].id=='negru':
                    lista.append(i)
        return lista
    elif len(zone[25])>0:
        lista=[25]
        return lista

def muta_piesa_neagra_disponibila(nr_zar):
    lista_2=[]
    lista_in_care_sa_caute=cauta_disponibilitate_piese_negre()
    for i in lista_in_care_sa_caute:
        if i-nr_zar>=1:
            if len(zone[i-nr_zar])>1:
                if zone[i-nr_zar][-1].id=='negru':
                    lista_2.append(i)
            if len(zone[i-nr_zar])==1:
                lista_2.append(i)
            if len(zone[i-nr_zar])==0:
                lista_2.append(i)
        if i-nr_zar<1:
            if verifica_piese_negre() is True:
                lista_2.append(i)
    return lista_2

def verifica_piese_maro():
    lista_piese_pe_tabla_maro=[]
    for i in range(1,19):
        if len(zone[i])>=1:
            if zone[i][-1].id=='maro':                       
                lista_piese_pe_tabla_maro.append(i)
    if len(lista_piese_pe_tabla_maro)==0:
        return True
    else:
        return False

def cauta_disponibilitate_piese_maro():
    lista=[]
    if len(zone[0])==0:
        for i in range(0,25):
            if len(zone[i])!=0:
                if zone[i][-1].id=='maro':
                    lista.append(i)
        return lista
    elif len(zone[0])>0:
        lista=[0]
        return lista

def muta_piesa_maro_disponibila(nr_zar):
    lista_2=[]
    lista_in_care_sa_caute=cauta_disponibilitate_piese_maro()
    for i in lista_in_care_sa_caute:
        if i+nr_zar<=24:
            if len(zone[i+nr_zar])>1:
                if zone[i+nr_zar][-1].id=='maro':
                    lista_2.append(i)
            if len(zone[i+nr_zar])==1:
                lista_2.append(i)
            if len(zone[i+nr_zar])==0:
                lista_2.append(i)
        if i+nr_zar>24:
            if verifica_piese_maro() is True:
                lista_2.append(i)
    return lista_2

def verifica_piese_inainte_a_scoate_negre(x):
    numar=0
    for i in range(x+1,7):
        if len(zone[i])!=0:
            if zone[i][-1].id=='negru': 
                numar+=1
    return numar

def verifica_piese_inainte_a_scoate_maro(x):
    numar=0
    for i in range(x-1,18,-1):
        if len(zone[i])!=0:
            if zone[i][-1].id=='maro':
                numar+=1
    return numar

def sorteza_zonele_dupa_y_crescator(lista):
    lista.sort(key=lambda obj: obj.y, reverse=False)

def sorteza_zonele_dupa_y_descrescator(lista):
    lista.sort(key=lambda obj: obj.y, reverse=True)

def joaca3():
    n=0
    m=0
    y_negru=460
    y_maro=23
    x_pt_ambele=990
    zone_primite=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    cheie_n=False
    cheie_m=False
    da_cu_zarul=False
    global tura_player1
    global val_zar_n    
    global val_zar_m
    global zar_n_selectat
    global zar_m_selectat
    global tura_player
    global f
    clock = pygame.time.Clock()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(None)
    
    try:
        client.connect((SERVER, 9090))
    except:
        nu_te_poti_conecta()
            
    while True:
        fereastra.fill(BLACK)
        fereastra.blit(text9,(370,360))
        pygame.display.update()
        try:
            nr_player=client.recv(1024)
            nr_player_1=pickle.loads(nr_player)
        except:pass
        if nr_player_1==2:
            joaca4=True
            break

    while joaca4:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                joaca4=False
                sys.exit() 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    if tura_player==True and zar_n_selectat==False and zar_m_selectat==False:
                        if f==1:
                            f-=1
                            cheie_m=False
                            cheie_n=False
                            n=random.randint(1,6)
                            m=random.randint(1,6)
                            if n==m:
                                lista_n_player.append(n)
                                lista_n_player.append(2)
                                lista_m_player.append(m)
                                lista_m_player.append(2)
                            if n!=m:
                                lista_n_player.append(n)
                                lista_n_player.append(1)
                                lista_m_player.append(m)
                                lista_m_player.append(1)
                        tura_player1=False
                        da_cu_zarul=False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and tura_player==True:
                    if lista_n_player[-2]<=6 and lista_n_player[-2]>0 and f==0:
                        val_zar_n=lista_n_player[-2]
                        cheie_n=True
                        cheie_m=False
                        zar_n_selectat=True
                        zar_m_selectat=False
                    else:
                        da_cu_zarul=True
                if event.key == pygame.K_m and tura_player==True:
                    if lista_m_player[-2]<=6 and lista_m_player[-2]>0 and f==0:
                        val_zar_m=lista_m_player[-2]
                        cheie_n=False
                        cheie_m=True
                        zar_n_selectat=False
                        zar_m_selectat=True
                    else:
                        da_cu_zarul=True
        
        fereastra.blit(imagine_fundal_final,(0,0))
        fereastra.blit(fundal_inceput_final,(0,700))
        fereastra.blit(text_player,(725,710))
        fereastra.blit(text_player1,(200,710))

        if tura_player==False:
            zaruri[n-1].draw(1000,245)
            zaruri[m-1].draw(1000,290)
            fereastra.blit(text_player1_la_mutare,(125,750))
        
        if tura_player==True:
            zaruri[n-1].draw(1000,362)
            zaruri[m-1].draw(1000,406)
            if cheie_n==True:
                pygame.draw.rect(fereastra,GREEN,(998,360,40,40),4)
            elif cheie_m==True:
                pygame.draw.rect(fereastra,GREEN,(998,404,40,40),4)
            if da_cu_zarul==True:
                fereastra.blit(text8,(680,750))
            dictionar={butoane[0].nr_buton:[str(butoane[0].zona),str(butoane[0].x),str(butoane[0].y)],
                        butoane[1].nr_buton:[str(butoane[1].zona),str(butoane[1].x),str(butoane[1].y)],
                        butoane[2].nr_buton:[str(butoane[2].zona),str(butoane[2].x),str(butoane[2].y)],
                        butoane[3].nr_buton:[str(butoane[3].zona),str(butoane[3].x),str(butoane[3].y)],
                        butoane[4].nr_buton:[str(butoane[4].zona),str(butoane[4].x),str(butoane[4].y)],
                        butoane[5].nr_buton:[str(butoane[5].zona),str(butoane[5].x),str(butoane[5].y)],
                        butoane[6].nr_buton:[str(butoane[6].zona),str(butoane[6].x),str(butoane[6].y)],
                        butoane[7].nr_buton:[str(butoane[7].zona),str(butoane[7].x),str(butoane[7].y)],
                        butoane[8].nr_buton:[str(butoane[8].zona),str(butoane[8].x),str(butoane[8].y)],
                        butoane[9].nr_buton:[str(butoane[9].zona),str(butoane[9].x),str(butoane[9].y)],
                        butoane[10].nr_buton:[str(butoane[10].zona),str(butoane[10].x),str(butoane[10].y)],
                        butoane[11].nr_buton:[str(butoane[11].zona),str(butoane[11].x),str(butoane[11].y)],
                        butoane[12].nr_buton:[str(butoane[12].zona),str(butoane[12].x),str(butoane[12].y)],
                        butoane[13].nr_buton:[str(butoane[13].zona),str(butoane[13].x),str(butoane[13].y)],
                        butoane[14].nr_buton:[str(butoane[14].zona),str(butoane[14].x),str(butoane[14].y)],
                        butoane[15].nr_buton:[str(butoane[15].zona),str(butoane[15].x),str(butoane[15].y)],
                        butoane[16].nr_buton:[str(butoane[16].zona),str(butoane[16].x),str(butoane[16].y)],
                        butoane[17].nr_buton:[str(butoane[17].zona),str(butoane[17].x),str(butoane[17].y)],
                        butoane[18].nr_buton:[str(butoane[18].zona),str(butoane[18].x),str(butoane[18].y)],
                        butoane[19].nr_buton:[str(butoane[19].zona),str(butoane[19].x),str(butoane[19].y)],
                        butoane[20].nr_buton:[str(butoane[20].zona),str(butoane[20].x),str(butoane[20].y)],
                        butoane[21].nr_buton:[str(butoane[21].zona),str(butoane[21].x),str(butoane[21].y)],
                        butoane[22].nr_buton:[str(butoane[22].zona),str(butoane[22].x),str(butoane[22].y)],
                        butoane[23].nr_buton:[str(butoane[23].zona),str(butoane[23].x),str(butoane[23].y)],
                        butoane[24].nr_buton:[str(butoane[24].zona),str(butoane[24].x),str(butoane[24].y)],
                        butoane[25].nr_buton:[str(butoane[25].zona),str(butoane[25].x),str(butoane[25].y)],
                        butoane[26].nr_buton:[str(butoane[26].zona),str(butoane[26].x),str(butoane[26].y)],
                        butoane[27].nr_buton:[str(butoane[27].zona),str(butoane[27].x),str(butoane[27].y)],
                        butoane[28].nr_buton:[str(butoane[28].zona),str(butoane[28].x),str(butoane[28].y)],
                        butoane[29].nr_buton:[str(butoane[29].zona),str(butoane[29].x),str(butoane[29].y)]                   
                    }
            date=[tura_player,tura_player1,dictionar,n,m]
            serialized_data = pickle.dumps(date)
            client.sendall(serialized_data)
        
        while True:
            try:
                serialized_data1 = client.recv(100000)
                tura_player_primit, tura_player1_primit, dictionar1, n, m= pickle.loads(serialized_data1)
            except Exception as e:
                print(e)
                client.close()
                player_s_a_deconectat()
                break

            for i in butoane:
                zona_noua=int(dictionar1[i.nr_buton][0])
                i.zona=zona_noua
                i.x=int(dictionar1[i.nr_buton][1])
                i.y=int(dictionar1[i.nr_buton][2])
                if zona_noua==-1:
                    zone_primite[-2].append(i)
                if zona_noua==26:
                    zone_primite[-1].append(i)
                if zona_noua!=-1 and zona_noua != 26:
                    zone_primite[zona_noua].append(i)
            for j in range(0,28):
                zone[j]=zone_primite[j]

            tura_player=tura_player_primit
            tura_player1=tura_player1_primit

            zone_primite=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

            for i in range(0,13):
                sorteza_zonele_dupa_y_descrescator(zone[i])
            
            for i in range(13,26):
                sorteza_zonele_dupa_y_crescator(zone[i])
            break

        for i in range(len(zone[-2])):
            fereastra.blit(piesa_neagra_scoasa1,(x_pt_ambele,y_negru))
            y_negru+=14
        y_negru=460
        for i in range(len(zone[-1])):
            fereastra.blit(piesa_maro_scoasa1,(x_pt_ambele,y_maro))
            y_maro+=14
        y_maro=23

        if lista_n_player[-1]==0 and lista_m_player[-1]==0:
            tura_player=False
            tura_player1=True
            cheie_n=False
            cheie_m=False
            zar_n_selectat=False
            zar_m_selectat=False
            f=1
            lista_m_player[-1]=-1
            lista_n_player[-1]=-1
            date1=[tura_player,tura_player1,dictionar1,n,m]
            serialized_data2 = pickle.dumps(date1)
            client.sendall(serialized_data2)

        deseneaza_butoane()

        if len(zone[-1])==15:
            fereastra.fill(BLACK)
            fereastra.blit(text10,(450,360))
            
        if len(zone[-2])==15:
            fereastra.fill(BLACK)
            fereastra.blit(text11,(450,360))
        
        pygame.display.update()

def joaca1():
    n=0
    m=0
    g=1
    joaca2=True
    cheie_n=False
    cheie_m=False
    da_cu_zarul=False
    global nr_random_pt_calculator
    global val_zar_n    
    global val_zar_m
    global val_zar_n_calculator    
    global val_zar_m_calculator
    global zar_n_selectat
    global zar_m_selectat
    global tura_player
    global tura_calculator
    global f
    y_negru=460
    y_maro=23
    x_pt_ambele=990
    clock = pygame.time.Clock()
 
    while joaca2:
        clock.tick(FPS)
        fereastra.blit(imagine_fundal_final,(0,0))
        fereastra.blit(fundal_inceput_final,(0,700))
        fereastra.blit(text_player,(725,710))
        fereastra.blit(text_calculator,(190,710))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                joaca2=False
                sys.exit() 
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    if tura_player==True and zar_n_selectat==False and zar_m_selectat==False:
                        if f==1:
                            f-=1
                            cheie_m=False
                            cheie_n=False
                            n=random.randint(1,6)
                            m=random.randint(1,6)
                            if n==m:
                                lista_n_player.append(n)
                                lista_n_player.append(2)
                                lista_m_player.append(m)
                                lista_m_player.append(2)
                            if n!=m:
                                lista_n_player.append(n)
                                lista_n_player.append(1)
                                lista_m_player.append(m)
                                lista_m_player.append(1)
                        tura_calculator=False
                        da_cu_zarul=False
                        g=1
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and tura_player==True:
                    if lista_n_player[-2]<=6 and lista_n_player[-2]>0:
                        val_zar_n=lista_n_player[-2]
                        cheie_n=True
                        cheie_m=False
                        zar_n_selectat=True
                        zar_m_selectat=False
                    else:
                        da_cu_zarul=True
                if event.key == pygame.K_m and tura_player==True:
                    if lista_m_player[-2]<=6 and lista_m_player[-2]>0:
                        val_zar_m=lista_m_player[-2]
                        cheie_n=False
                        cheie_m=True
                        zar_n_selectat=False
                        zar_m_selectat=True
                    else:
                        da_cu_zarul=True
                        
        if tura_player==True:
            zaruri[n-1].draw(1000,362)
            zaruri[m-1].draw(1000,406)
            if cheie_n==True:
                pygame.draw.rect(fereastra,GREEN,(998,360,40,40),4)
            elif cheie_m==True:
                pygame.draw.rect(fereastra,GREEN,(998,404,40,40),4)
            if da_cu_zarul==True:
                fereastra.blit(text8,(680,750))
 
        if lista_n_player[-1]==0 and lista_m_player[-1]==0:
            tura_calculator=True
            tura_player=False
 
        if len(zona_1)==15:
            tura_calculator=False
            tura_player=False
            ecran_final_negru1()
 
        if len(zona26)==15:
            tura_calculator=False
            tura_player=False
            ecran_final_maro1()
 
        if tura_calculator==True:
            fereastra.blit(text_calculator_la_mutare,(100,750))
            if g>0:
                val_zar_n_calculator=random.randint(1,6)
                val_zar_m_calculator=random.randint(1,6)
                if val_zar_n_calculator==val_zar_m_calculator:
                    lista_n_calculator.append(val_zar_n_calculator)
                    lista_n_calculator.append(2)
                    lista_m_calculator.append(val_zar_m_calculator)
                    lista_m_calculator.append(2)
                    g-=1
                if val_zar_n_calculator!=val_zar_m_calculator:
                    lista_n_calculator.append(val_zar_n_calculator)
                    lista_n_calculator.append(1)
                    lista_m_calculator.append(val_zar_m_calculator)
                    lista_m_calculator.append(1)
                    g-=1
                pygame.time.delay(1500)
 
            zaruri[lista_n_calculator[-2]-1].draw(1000,245)
            zaruri[lista_m_calculator[-2]-1].draw(1000,290)

            for i in range(len(zona_1)):
                fereastra.blit(piesa_neagra_scoasa1,(x_pt_ambele,y_negru))
                y_negru+=14
            y_negru=460
            for i in range(len(zona26)):
                fereastra.blit(piesa_maro_scoasa1,(x_pt_ambele,y_maro))
                y_maro+=14
            y_maro=23
            
            n1=muta_piesa_maro_disponibila(lista_n_calculator[-2])
            
            if len(n1)==0:
                m1=muta_piesa_maro_disponibila(lista_m_calculator[-2])
                if len(m1)>=1:
                    if lista_m_calculator[-1]>=1:
                        nr_random_pt_calculator=random.choice(m1)
                        if len(zone[nr_random_pt_calculator])!=0:
                            if (zone[nr_random_pt_calculator][-1].zona+lista_m_calculator[-2])<=24:
                                if zone[nr_random_pt_calculator][-1].id=='maro':
                                    if len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])==0:
                                        zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                        lista_m_calculator[-1]-=1
                                        zone[nr_random_pt_calculator][-1].schimba_poz()
                                        zone[nr_random_pt_calculator][-1].draw1()
                                        time.sleep(1)
                                        zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    elif len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])==1:
                                        if zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='negru':
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].zona=25
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].schimba_poz()
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].draw1()
                                            time.sleep(1)
                                            zone[25].append(zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1])
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]].remove(zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1])
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        elif zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='maro':
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[nr_random_pt_calculator][-1].draw1()
                                            time.sleep(1)
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    elif len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])>=2:
                                        if zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='maro':
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[nr_random_pt_calculator][-1].draw1()
                                            time.sleep(1)
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                else:
                                    pass
                            elif (zone[nr_random_pt_calculator][-1].zona+lista_m_calculator[-2])>24:
                                if (25-zone[nr_random_pt_calculator][-1].zona)==lista_m_calculator[-2]:
                                    zone[-1].append(zone[nr_random_pt_calculator][-1])
                                    zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    zone[-1][-1].zona=26
                                    zone[-1][-1].schimba_poz()
                                    lista_m_calculator[-1]-=1
                                elif (25-zone[nr_random_pt_calculator][-1].zona)!=lista_m_calculator[-2]:
                                    if verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)==0:
                                        zone[-1].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        zone[-1][-1].zona=26
                                        zone[-1][-1].schimba_poz()
                                        lista_m_calculator[-1]-=1
                                    elif verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)!=0:
                                        pass
                                pygame.time.delay(1000)

                    n1=muta_piesa_maro_disponibila(lista_n_calculator[-2])
                    if len(n1)==0:
                        lista_n_calculator[-1]=0  
                elif len(m1)==0:
                    lista_m_calculator[-1]=0
                    lista_n_calculator[-1]=0
                for i in range(len(zona26)):
                    fereastra.blit(piesa_maro_scoasa1,(x_pt_ambele,y_maro))
                    y_maro+=14
                y_maro=23
            elif len(n1)>=1:
                if lista_n_calculator[-1]>=1:
                    nr_random_pt_calculator=random.choice(n1)
                    if len(zone[nr_random_pt_calculator])!=0:
                        if (zone[nr_random_pt_calculator][-1].zona+lista_n_calculator[-2])<=24:
                            if zone[nr_random_pt_calculator][-1].id=='maro':
                                if len(zone[nr_random_pt_calculator+lista_n_calculator[-2]])==0:
                                    zone[nr_random_pt_calculator][-1].zona+=lista_n_calculator[-2]
                                    lista_n_calculator[-1]-=1
                                    zone[nr_random_pt_calculator][-1].schimba_poz()
                                    zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                    zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    deseneaza_butoane1()
                                    pygame.display.update()
                                    time.sleep(1)
                                elif len(zone[nr_random_pt_calculator+lista_n_calculator[-2]])==1:
                                    if zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1].id=='negru':
                                        zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1].zona=25
                                        zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1].schimba_poz()
                                        zone[25].append(zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1])
                                        zone[nr_random_pt_calculator+lista_n_calculator[-2]].remove(zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1])
                                        zone[nr_random_pt_calculator][-1].zona+=lista_n_calculator[-2]
                                        lista_n_calculator[-1]-=1
                                        zone[nr_random_pt_calculator][-1].schimba_poz()
                                        zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        deseneaza_butoane1()
                                        pygame.display.update()
                                        time.sleep(1)
                                    elif zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1].id=='maro':
                                        zone[nr_random_pt_calculator][-1].zona+=lista_n_calculator[-2]
                                        lista_n_calculator[-1]-=1
                                        zone[nr_random_pt_calculator][-1].schimba_poz()
                                        zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        deseneaza_butoane1()
                                        pygame.display.update()
                                        time.sleep(1)
                                elif len(zone[nr_random_pt_calculator+lista_n_calculator[-2]])>=2:
                                    if zone[nr_random_pt_calculator+lista_n_calculator[-2]][-1].id=='maro':
                                        zone[nr_random_pt_calculator][-1].zona+=lista_n_calculator[-2]
                                        lista_n_calculator[-1]-=1
                                        zone[nr_random_pt_calculator][-1].schimba_poz()
                                        zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        deseneaza_butoane1()
                                        pygame.display.update()
                                        time.sleep(1)
                            else:
                                pass
                        elif (zone[nr_random_pt_calculator][-1].zona+lista_n_calculator[-2])>24:
                            if (25-zone[nr_random_pt_calculator][-1].zona)==lista_n_calculator[-2]:
                                zone[-1].append(zone[nr_random_pt_calculator][-1])
                                zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                zone[-1][-1].zona=26
                                zone[-1][-1].schimba_poz()
                                lista_n_calculator[-1]-=1
                            elif (25-zone[nr_random_pt_calculator][-1].zona)!=lista_n_calculator[-2]:
                                if verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)==0:
                                    zone[-1].append(zone[nr_random_pt_calculator][-1])
                                    zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    zone[-1][-1].zona=26
                                    zone[-1][-1].schimba_poz()
                                    lista_n_calculator[-1]-=1
                                elif verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)!=0:
                                    pass
                            pygame.time.delay(1000)
                    pygame.time.delay(500)            
                m1=muta_piesa_maro_disponibila(lista_m_calculator[-2])
                if len(m1)>=1:
                    if lista_m_calculator[-1]>=1:
                        nr_random_pt_calculator=random.choice(m1)
                        if len(zone[nr_random_pt_calculator])!=0:
                            if (zone[nr_random_pt_calculator][-1].zona+lista_m_calculator[-2])<=24:
                                if zone[nr_random_pt_calculator][-1].id=='maro':
                                    if len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])==0:
                                        zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                        lista_m_calculator[-1]-=1
                                        zone[nr_random_pt_calculator][-1].schimba_poz()
                                        zone[nr_random_pt_calculator][-1].draw1()
                                        time.sleep(1)
                                        zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    elif len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])==1:
                                        if zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='negru':
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].zona=25
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].schimba_poz()
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].draw1()
                                            time.sleep(1)
                                            zone[25].append(zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1])
                                            zone[nr_random_pt_calculator+lista_m_calculator[-2]].remove(zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1])
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        elif zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='maro':
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[nr_random_pt_calculator][-1].draw1()
                                            time.sleep(1)
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    elif len(zone[nr_random_pt_calculator+lista_m_calculator[-2]])>=2:
                                        if zone[nr_random_pt_calculator+lista_m_calculator[-2]][-1].id=='maro':
                                            zone[nr_random_pt_calculator][-1].zona+=lista_m_calculator[-2]
                                            lista_m_calculator[-1]-=1
                                            zone[nr_random_pt_calculator][-1].schimba_poz()
                                            zone[nr_random_pt_calculator][-1].draw1()
                                            time.sleep(1)
                                            zone[zone[nr_random_pt_calculator][-1].zona].append(zone[nr_random_pt_calculator][-1])
                                            zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                else:
                                    pass
                            elif (zone[nr_random_pt_calculator][-1].zona+lista_m_calculator[-2])>24:
                                if (25-zone[nr_random_pt_calculator][-1].zona)==lista_m_calculator[-2]:
                                    zone[-1].append(zone[nr_random_pt_calculator][-1])
                                    zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                    zone[-1][-1].zona=26
                                    zone[-1][-1].schimba_poz()
                                    lista_m_calculator[-1]-=1
                                elif (25-zone[nr_random_pt_calculator][-1].zona)!=lista_m_calculator[-2]:
                                    if verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)==0:
                                        zone[-1].append(zone[nr_random_pt_calculator][-1])
                                        zone[nr_random_pt_calculator].remove(zone[nr_random_pt_calculator][-1])
                                        zone[-1][-1].zona=26
                                        zone[-1][-1].schimba_poz()
                                        lista_m_calculator[-1]-=1
                                    elif verifica_piese_inainte_a_scoate_maro(zone[nr_random_pt_calculator][-1].zona)!=0:
                                        pass
                                pygame.time.delay(1000)
 
                elif len(m1)<=0:
                    lista_m_calculator[-1]=0
                for i in range(len(zona26)):
                    fereastra.blit(piesa_maro_scoasa1,(x_pt_ambele,y_maro))
                    y_maro+=14
                y_maro=23
            if lista_n_calculator[-1]==0 and lista_m_calculator[-1]==0:
                tura_calculator=False
                tura_player=True
                zar_n_selectat=False
                zar_m_selectat=False
                cheie_m=False
                cheie_n=False
                f=1
                fereastra.blit(imagine_fundal_final,(0,0))
                fereastra.blit(fundal_inceput_final,(0,700))
                fereastra.blit(text_player,(725,710))
                fereastra.blit(text_calculator,(190,710))
                text = font.render('Poti muta', True, GREEN)
                fereastra.blit(text, (695,750))
                zaruri[lista_n_calculator[-2]-1].draw(1000,245)
                zaruri[lista_m_calculator[-2]-1].draw(1000,290)
        deseneaza_butoane()

        for i in range(len(zone)):
            if len(zone[i])==0:
                pass
            if len(zone[i])>5:
                pygame.draw.circle(fereastra,RED,(zone[i][-1].x+39,zone[i][-1].y+39),30,8)
        
        for i in range(len(zona_1)):
            fereastra.blit(piesa_neagra_scoasa1,(x_pt_ambele,y_negru))
            y_negru+=14
        y_negru=460
        for i in range(len(zona26)):
            fereastra.blit(piesa_maro_scoasa1,(x_pt_ambele,y_maro))
            y_maro+=14
        y_maro=23

        pygame.display.update()

def meniu():
    meniu=True
    while meniu:
        fereastra.blit(fundal_inceput_final,(0,0))
        fereastra.blit(buton_de_start_final,(450,260))
        fereastra.blit(buton_de_stop_final,(450,440))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meniu=False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 450 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[0] <= 650 and pygame.mouse.get_pos()[1]<=360:
                    if pygame.mouse.get_pressed()[0]:
                        ecran_de_ales()
                if pygame.mouse.get_pos()[0] >= 450 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[0] <= 650 and pygame.mouse.get_pos()[1]<=540:
                    if pygame.mouse.get_pressed()[0]:
                        sys.exit()
            
        pygame.display.update()

def ecran_final_negru1():
    global joaca2
    ecran_final_negru=True
    joaca2=False
    while ecran_final_negru:
        fereastra.fill(BLACK)
        text = font1.render('Jucatorul a castigat', True, GREEN)
        fereastra.blit(text, (350,320))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def ecran_final_maro1():
    global joaca2
    ecran_final_maro=True
    joaca2=False
    while ecran_final_maro:
        fereastra.fill(BLACK)
        text = font1.render('Calculatorul a castigat', True, GREEN)
        fereastra.blit(text, (335,320))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def ecran_de_ales():
    
    ecran_de_ales=True
    fereastra.blit(fundal_inceput_final,(0,0))
    fereastra.blit(imagine_de_ales_final,(305,120))
    fereastra.blit(imagine_de_ales_final1,(305,340))

    while ecran_de_ales:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ecran_de_ales=False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 305 and pygame.mouse.get_pos()[1] >= 250 and pygame.mouse.get_pos()[0] <= 805 and pygame.mouse.get_pos()[1]<=370:
                    if pygame.mouse.get_pressed()[0]:
                        ecran_de_ales=False
                        joaca1()
                if pygame.mouse.get_pos()[0] >= 305 and pygame.mouse.get_pos()[1] >= 472 and pygame.mouse.get_pos()[0] <= 806 and pygame.mouse.get_pos()[1]<=591:
                    if pygame.mouse.get_pressed()[0]:
                        joaca3()
                        ecran_de_ales=False
        pygame.display.update()

def nu_te_poti_conecta():
    
    nu_te_poti_conecta1=True
    fereastra.fill(BLACK)
    fereastra.blit(text12,(310,310))
    fereastra.blit(buton_menu,(345,340))
    while nu_te_poti_conecta1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nu_te_poti_conecta1=False
                sys.exit()
            if pygame.mouse.get_pos()[0] >= 360 and pygame.mouse.get_pos()[1] >= 460 and pygame.mouse.get_pos()[0] <= 745 and pygame.mouse.get_pos()[1]<=570:
                if pygame.mouse.get_pressed()[0]:
                    meniu()
                    nu_te_poti_conecta1=False
        pygame.display.update()

def player_s_a_deconectat():
    
    player_s_a_deconectat1=True
    fereastra.fill(BLACK)
    fereastra.blit(text13,(235,330))
    while player_s_a_deconectat1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_s_a_deconectat1=False
                sys.exit()
        pygame.display.update()

meniu()