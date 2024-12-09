""" ============================
Zadanie 136. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowe
================================"""
from time import sleep


def print_board(board):
    """
    Prints an NxN board in a visually appealing way.

    :param board: 2D list representing the board.
    """
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))


def jump_diff(T :list[list[int]], y:int, x:int, j :int)->tuple[int,int]:
    jx = (-2,-1,1,2,2,1,-1,-2)
    jy = (1,2,2,1,-1,-2,-2,-1)
    if 0 <= y+jy[j] < len(T) and 0 <= x + jx[j] < len(T):
        return (jy[j], jx[j])
    return (-1,-1)

def knight_fills_arrray(T :list[list[int]], y :int, x :int, i :int=1) -> bool:
    T[y][x] = i
    if len(T)*len(T[0]) == i:
        return True
    for j in range(8):
        jump_d = jump_diff(T,y,x,j)
        if jump_d != (-1,-1) and T[y + jump_d[0]][x + jump_d[1]] ==0:
            if knight_fills_arrray(T,y + jump_d[0],x + jump_d[1],i+1):
                return True
    T[y][x] = 0
    return False



T1 = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]
]
knight_fills_arrray(T1, 0, 0)
print_board(T1)


T1 = [
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
]

knight_fills_arrray(T1, 3,2)

print_board(T1)
