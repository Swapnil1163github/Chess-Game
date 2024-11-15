from const import *
from square import Square
from piece import *
from move import Move

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    def calc_moves(self , piece , row , col):

        #CALCALILATE ALL THE POSSIBLE OR VALID MOVES OF SPECIFIC PIECE IN THAT POSITION

        def pawn_moves():
            #steps of the pawn
            steps =1 if piece.moved else 2

            #vertical moves 
            start = row + piece.dir
            end = row + (piece.dir * (1+steps))
            for move_row in range(start , end , piece.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        #create an initial and fianl move squares
                        initial = Square(row , col)
                        final = Square(move_row , col)
                        #create a new move
                        move = Move(initial , final)
                        piece.add_moves(move)
                    #blocked 
                    else:
                        break
                    #this is not in range
                else:  break

            #diagonal Moves
    

        def knight_moves():
            #there are 8 possible moves if it is at the center of the board
            possible_moves = [

            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),

            ]

            for possible_move in possible_moves:
                possible_move_row , possible_move_col = possible_move

                if Square.in_range(possible_move_row , possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        
                        #create the squares of the new move 
                        initial = Square(row , col)
                        final = Square(possible_move_row , possible_move_col) #here piece = piece

                        #create a new move
                        move = Move(initial,final )
                        #append a new valid move
                        piece.add_moves(move)

        if isinstance(piece , Pawn):
            pawn_moves()

        elif isinstance(piece , Knight):
            knight_moves()

        elif isinstance(piece , Bishop):
            pass

        elif isinstance(piece , Rook):
            pass

        elif isinstance(piece , Queen):
            pass

        elif isinstance(piece , King):
            pass

    def _create(self):
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self , color):
        row_pawn , row_other = (6,7) if color == 'white' else (1,0)

        #pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn , col , Pawn(color))

        #kinghts
        self.squares[row_other][1] = Square(row_other , 1 , Knight(color))
        self.squares[row_other][6] = Square(row_other , 6 , Knight(color))


        #bishop
        self.squares[row_other][2] = Square(row_other , 2 , Bishop(color))
        self.squares[row_other][5] = Square(row_other , 5 , Bishop(color))

        #rooks
        self.squares[row_other][0] = Square(row_other , 0 , Rook(color))
        self.squares[row_other][7] = Square(row_other , 7 , Rook(color))

        #queen
        self.squares[row_other][3] = Square(row_other , 3 , Queen(color))

        #king
        self.squares[row_other][4] = Square(row_other , 4 , King(color))
   