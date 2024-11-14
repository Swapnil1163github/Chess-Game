
class Square:

    def __init__(self , row , col , piece = None):
        self.col = col
        self.row = row
        self.piece = piece

    def has_piece(self):
        return self.piece != None