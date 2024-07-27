"""
Script: app.py
Author: Felipe de Paula Gabriel
Date: 2024-06-09
Version : 1.0
Description: Script principal do Ultimate Tic Tac Toe. A versão 1.0 é um jogo da velha tradicional
para terminal.
"""

from backend.tic_tac_toe import TicTacToe

if __name__ == "__main__":

    game = TicTacToe("X")
    print("=========== Bem Vindo ao Jogo da Velha ===========\n")
    game.play()
