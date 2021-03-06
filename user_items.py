#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import system

class UserPlanet(Sprite):
    image = None
    def __init__(self,x,y,w,h,start_mass,group,temp,obstacles_grp,bar,player,kind,goal,image):
        Sprite.__init__(self)
        if self.image == None:
            self.image = system.load_graphics(image)
        self.image = pygame.transform.smoothscale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mass = start_mass
        self.reGroup = False
        self.group = group
        self.grabbed = True
        self.mouse_offset = ((26,26))
        self.temp = temp
        self.add(temp)
        self.bar = bar
        self.ob_grp = obstacles_grp
        self.og_place = ((x,y))
        self.player = player
        self.kind = kind
        self.goal = goal
                
    def update(self,pos,other=None):
        xchange,ychange = pos
        xoff,yoff = self.mouse_offset
        newX = xchange-xoff
        newY = ychange-yoff
        if newX >= 1 and newX <= 999 and newY >= 1 and self.grabbed:
            self.rect.x = newX
            self.rect.y = newY
        if self.rect.y+self.rect.h < 620 and self.reGroup == False:
            self.reGroup = True
 
    def dropped(self):
        self.grabbed = False
        self.kill()
        if not pygame.sprite.collide_mask(self,self.player) and self.rect.y < 619 and not pygame.sprite.collide_mask(self,self.goal):
            self.add(self.group)
            self.add(self.ob_grp)
        else:
            if self.kind == 1:
                self.bar.item_one_reset()
            elif self.kind == 2:
                self.bar.item_two_reset()
            elif self.kind == 3:
                self.bar.item_three_reset()
    
    def grab(self,pos):
        x,y = pos
        self.og_place = (self.rect.x,self.rect.y)
        xoffset = x-self.rect.x
        yoffset = y-self.rect.y
        self.mouse_offset = ((xoffset,yoffset))
        self.grabbed = True

    def drop(self,blackHoles):
        self.grabbed = False
        if self.rect.y > 619 and self.reGroup == True:
            self.bar.items_one_placed -= 1
            self.bar.items_one.x = 119
            self.kill()
            if self.kind == 1:
                self.bar.item_one_reset()
            elif self.kind == 2:
                self.bar.item_two_reset()
            elif self.kind == 3:
                self.bar.item_three_reset()
        elif pygame.sprite.collide_mask(self,self.player) or pygame.sprite.spritecollideany(self,blackHoles) or pygame.sprite.collide_mask(self,self.goal):
            x,y = self.og_place
            self.rect.x = x
            self.rect.y = y

    def draw(self,surf):
        surf.blit(self.image,(self.rect.x,self.rect.y))


    def remove(self):
        self.kill()
        if self.kind == 1:
            self.bar.item_one_reset()
        elif self.kind == 2:
            self.bar.item_two_reset()
        elif self.kind == 3:
            self.bar.item_three_reset()
