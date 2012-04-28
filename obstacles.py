#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import system

class BlackHole(Sprite):
    image = None
    def __init__(self,x,y,group,surf,w,h,mass,image=str('black_hole.png')):
        Sprite.__init__(self)
        if self.image == None:
            self.image = system.load_graphics(image)
        self.image = self.scale(w,h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.group = group
        self.add(self.group)
        self.mass = mass
        self.surface = surf

    def scale(self,w,h):
        return pygame.transform.scale(self.image, (w,h))
        
    def move(self,newx,newy):
        self.rect.x = newx
        self.rect.y = newy

    def flip(self):
        self.image = pygame.transform.flip(self.image,True,False)
    
    def update(self):
        pass



class Alien(Sprite):
    image = None
    def __init__(self,x,y,group,surf,size,kind):
        Sprite.__init__(self)
        image_choices = [(str("alien0.png")),(str("alien1.png")),
                         (str("alien2.png"))]
        if self.image == None:
            self.image = system.load_graphics(image_choices[kind])
        self.image = self.scale(size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.group = group
        self.add(self.group)
        self.kind = kind
        self.surface = surf

    def scale(self,size):
        h = size
        w = int(size*2.09790)
        return pygame.transform.smoothscale(self.image, (w,h))

    def move(self,newx,newy):
        self.rect.x = newx
        self.rect.y = newy

    def rotate(self,angle):
        self.image = pygame.transform.rotate(self.image,angle)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
            
        

class EarthRounder(Alien):
    def __init__(self,x,y,group,surf,size,kind):
        Alien.__init__(self,x,y,group,surf,size,kind)
        self.forth = True

    def update(self):
        #min x = 513
        #max x = 622
        #min y = 285
        #max y = 313
        if self.rect.x < 620 and self.forth:
            self.rect.x += 2
            
            #self.rect.y -= 3
        elif self.rect.x > 514 and not self.forth:
            self.rect.x -= 2
            #self.rect.y += 3
        elif self.rect.x >= 620:
            self.forth = False
        else:
            self.forth = True

        if self.rect.x < 600 and self.forth:
            self.rect.y -= 3
        elif self.rect.x > 600 and self.forth:
            self.rect.y += 2

        elif self.rect.x > 600 and not self.forth:
            self.rect.y -= 2
        elif self.rect.x < 600 and not self.forth:
            self.rect.y += 3

class BlueUpAnDown(Alien):
    def __init__(self,x,y,group,surf,size,kind):
        Alien.__init__(self,x,y,group,surf,size,kind)
        self.forth = False
        self.shouldUpdate = 0

    def update(self):
        if self.shouldUpdate == 1:
            if self.rect.y > 97 and not self.forth:
                self.rect.y -= 1
            elif self.rect.y < 239 and self.forth:
                self.rect.y += 1
            elif self.rect.y >= 239:
                self.forth = False
            else:
                self.forth = True
            self.shouldUpdate = 0
        else:
            self.shouldUpdate += 1
