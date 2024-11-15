import pygame

from const import *
class Dragger:

    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging = False


    #BLIT METHODS ARE HERE 

    def update_blit(self , surface):
        #this is the texture
        self.piece.set_texture(size = 128)
        texture = self.piece.texture

        #this is img
        img = pygame.image.load(texture)

        #this is rectangle
        img_center = (self.mouseX , self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)

        #blit
        surface.blit(img, self.piece.texture_rect)

    #THIS ARE OTHER METHODS

    def update_mouse(self , pos):
        self.mouseX , self.mouseY = pos #(x cor , y cor)

    def save_initial(self , pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self , piece ):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False