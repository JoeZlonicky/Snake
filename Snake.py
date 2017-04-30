import pygame
import SnakePiece
from enum import Enum
import copy

class Direction(Enum):
    NONE = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Snake:
    def __init__(self):
        self.block_size = 16
        starting_piece_1 = SnakePiece.SnakePiece(48, 0)
        starting_piece_2 = SnakePiece.SnakePiece(32, 0)
        starting_piece_3 = SnakePiece.SnakePiece(16, 0)
        starting_piece_4 = SnakePiece.SnakePiece(0, 0)
        self.pieces = [starting_piece_1, starting_piece_2, starting_piece_3, starting_piece_4]
        self.direction = Direction.NONE
        self.growing = False

    def ChangeDirection(self, direction):
        new_direction = direction.value % 2
        current_direction = self.direction.value % 2
        if not new_direction == current_direction:
            self.direction = direction

    def Move(self):
        if self.direction == Direction.UP:
            self.MoveY(-self.block_size)
        elif self.direction == Direction.RIGHT:
            self.MoveX(self.block_size)
        elif self.direction == Direction.DOWN:
            self.MoveY(self.block_size)
        elif self.direction == Direction.LEFT:
            self.MoveX(-self.block_size)

    def MoveX(self, x):
        held_position = copy.copy(self.pieces[0].rect)
        self.pieces[0].rect.x += x
        self.MoveRestOfPieces(held_position)

    def MoveY(self, y):
        held_position = copy.copy(self.pieces[0].rect)
        self.pieces[0].rect.y += y
        self.MoveRestOfPieces(held_position)

    def MoveRestOfPieces(self, position_of_first_piece):
        held_position = position_of_first_piece
        for piece in self.pieces[1:]:
            previous_position = copy.copy(piece.rect)
            piece.rect = copy.copy(held_position)
            held_position = copy.copy(previous_position)
            if piece == self.pieces[-1]:
                if self.growing:
                    new_piece = SnakePiece.SnakePiece(held_position.x, held_position.y)
                    self.pieces.append(new_piece)
                    self.growing = False

    def BerryEaten(self):
        self.growing = True